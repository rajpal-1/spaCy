from typing import Optional
from pathlib import Path
from wasabi import msg
import re
import shutil
import requests

from ...util import ensure_path, working_dir
from .._util import project_cli, Arg, PROJECT_FILE, load_project_config, get_checksum
from .._util import download_file, git_sparse_checkout


# TODO: find a solution for caches
# CACHES = [
#     Path.home() / ".torch",
#     Path.home() / ".caches" / "torch",
#     os.environ.get("TORCH_HOME"),
#     Path.home() / ".keras",
# ]


@project_cli.command("assets")
def project_assets_cli(
    # fmt: off
    project_dir: Path = Arg(Path.cwd(), help="Path to cloned project. Defaults to current working directory.", exists=True, file_okay=False),
    # fmt: on
):
    """Fetch project assets like datasets and pretrained weights. Assets are
    defined in the "assets" section of the project.yml. If a checksum is
    provided in the project.yml, the file is only downloaded if no local file
    with the same checksum exists.
    """
    project_assets(project_dir)


def project_assets(project_dir: Path) -> None:
    """Fetch assets for a project using DVC if possible.

    project_dir (Path): Path to project directory.
    """
    project_path = ensure_path(project_dir)
    config = load_project_config(project_path)
    assets = config.get("assets", {})
    if not assets:
        msg.warn(f"No assets specified in {PROJECT_FILE}", exits=0)
    msg.info(f"Fetching {len(assets)} asset(s)")
    for asset in assets:
        dest = Path(asset["dest"])
        checksum = asset.get("checksum")
        if "git" in asset:
            print(dest)
            git_sparse_checkout(asset["git"]["repo"], asset["git"]["path"], dest)
        else:
            url = asset.get("url")
            if not url:
                # project.yml defines asset without URL that the user has to place
                check_private_asset(dest, checksum)
                continue
            fetch_asset(project_path, url, dest, checksum)


def check_private_asset(dest: Path, checksum: Optional[str] = None) -> None:
    """Check and validate assets without a URL (private assets that the user
    has to provide themselves) and give feedback about the checksum.

    dest (Path): Desintation path of the asset.
    checksum (Optional[str]): Optional checksum of the expected file.
    """
    if not Path(dest).exists():
        err = f"No URL provided for asset. You need to add this file yourself: {dest}"
        msg.warn(err)
    else:
        if checksum and checksum == get_checksum(dest):
            msg.good(f"Asset exists with matching checksum: {dest}")
        else:
            msg.fail(f"Asset available but with incorrect checksum: {dest}")


def fetch_asset(
    project_path: Path, url: str, dest: Path, checksum: Optional[str] = None
) -> None:
    """Fetch an asset from a given URL or path. If a checksum is provided and a
    local file exists, it's only re-downloaded if the checksum doesn't match.

    project_path (Path): Path to project directory.
    url (str): URL or path to asset.
    checksum (Optional[str]): Optional expected checksum of local file.
    RETURNS (Optional[Path]): The path to the fetched asset or None if fetching
        the asset failed.
    """
    # TODO: add support for caches
    dest_path = (project_path / dest).resolve()
    if dest_path.exists() and checksum:
        # If there's already a file, check for checksum
        if checksum == get_checksum(dest_path):
            msg.good(f"Skipping download with matching checksum: {dest}")
            return dest_path
    # We might as well support the user here and create parent directories in
    # case the asset dir isn't listed as a dir to create in the project.yml
    if not dest_path.parent.exists():
        dest_path.parent.mkdir(parents=True)
    with working_dir(project_path):
        url = convert_asset_url(url)
        try:
            download_file(url, dest_path)
            msg.good(f"Downloaded asset {dest}")
        except requests.exceptions.RequestException as e:
            if Path(url).exists() and Path(url).is_file():
                # If it's a local file, copy to destination
                shutil.copy(url, str(dest_path))
                msg.good(f"Copied local asset {dest}")
            else:
                msg.fail(f"Download failed: {dest}", e)
                return
    if checksum and checksum != get_checksum(dest_path):
        msg.fail(f"Checksum doesn't match value defined in {PROJECT_FILE}: {dest}")


def convert_asset_url(url: str) -> str:
    """Check and convert the asset URL if needed.

    url (str): The asset URL.
    RETURNS (str): The converted URL.
    """
    # If the asset URL is a regular GitHub URL it's likely a mistake
    if re.match(r"(http(s?)):\/\/github.com", url):
        converted = url.replace("github.com", "raw.githubusercontent.com")
        converted = re.sub(r"/(tree|blob)/", "/", converted)
        msg.warn(
            "Downloading from a regular GitHub URL. This will only download "
            "the source of the page, not the actual file. Converting the URL "
            "to a raw URL.",
            converted,
        )
        return converted
    return url
