from typing import (
    Callable,
    Iterator,
    Optional,
    Union,
    Tuple,
    List,
    Dict,
    Any,
)
from thinc.types import Floats1d, FloatsXd
from . import Language
from .strings import StringStore
from .lexeme import Lexeme
from .lookups import Lookups
from .morphology import Morphology
from .tokens import Doc, Span
from .vectors import Vectors
from pathlib import Path

def create_vocab(
    lang: Language, defaults: Any, vectors_name: Optional[str] = ...
) -> Vocab: ...

class Vocab:
    cfg: Dict[str, Any]
    get_noun_chunks: Optional[Callable[[Union[Doc, Span]], Iterator[Span]]]
    lookups: Lookups
    morphology: Morphology
    strings: StringStore
    vectors: Vectors
    writing_system: Dict[str, Any]

    def __init__(
        self,
        lex_attr_getters: Optional[Dict[str, Callable[[str], Any]]] = ...,
        strings: Optional[Union[List[str], StringStore]] = ...,
        lookups: Optional[Lookups] = ...,
        oov_prob: float = ...,
        vectors_name: Optional[str] = ...,
        writing_system: Dict[str, Any] = ...,
        get_noun_chunks: Optional[Callable[[Union[Doc, Span]], Iterator[Span]]] = ...,
    ) -> None: ...
    @property
    def lang(self) -> Language: ...
    def __len__(self) -> int: ...
    def add_flag(
        self, flag_getter: Callable[[str], bool], flag_id: int = ...
    ) -> int: ...
    def __contains__(self, key: str) -> bool: ...
    def __iter__(self) -> Iterator[Lexeme]: ...
    def __getitem__(self, id_or_string: Union[str, int]) -> Lexeme: ...
    @property
    def vectors_length(self) -> int: ...
    def reset_vectors(
        self, *, width: Optional[int] = ..., shape: Optional[int] = ...
    ) -> None: ...
    def prune_vectors(self, nr_row: int, batch_size: int = ...) -> Dict[str, float]: ...
    def get_vector(
        self,
        orth: Union[int, str],
        minn: Optional[int] = ...,
        maxn: Optional[int] = ...,
    ) -> FloatsXd: ...
    def set_vector(self, orth: Union[int, str], vector: Floats1d) -> None: ...
    def has_vector(self, orth: Union[int, str]) -> bool: ...
    def to_disk(
        self, path: Union[str, Path], *, exclude: Union[List[str], Tuple[str]] = ...
    ) -> None: ...
    def from_disk(
        self, path: Union[str, Path], *, exclude: Union[List[str], Tuple[str]] = ...
    ) -> Vocab: ...
    def to_bytes(self, *, exclude: Union[List[str], Tuple[str]] = ...) -> bytes: ...
    def from_bytes(
        self, bytes_data: bytes, *, exclude: Union[List[str], Tuple[str]] = ...
    ) -> Vocab: ...

def pickle_vocab(vocab: Vocab) -> Any: ...
def unpickle_vocab(
    sstore: StringStore,
    vectors: Any,
    morphology: Any,
    data_dir: Any,
    lex_attr_getters: Any,
    lookups: Any,
    get_noun_chunks: Any,
) -> Vocab: ...
