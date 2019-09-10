# coding: utf-8
from __future__ import unicode_literals

import srsly
from collections import OrderedDict

from .errors import Errors
from .util import SimpleFrozenDict, ensure_path
from .strings import hash_string

from . import util

import srsly
from preshed.bloom import BloomFilter

class Lookups(object):
    """Container for large lookup tables and dictionaries, e.g. lemmatization
    data or tokenizer exception lists. Lookups are available via vocab.lookups,
    so they can be accessed before the pipeline components are applied (e.g.
    in the tokenizer and lemmatizer), as well as within the pipeline components
    via doc.vocab.lookups.

    """

    def __init__(self):
        """Initialize the Lookups object.

        RETURNS (Lookups): The newly created object.
        """
        self._tables = OrderedDict()

    def __contains__(self, name):
        """Check if the lookups contain a table of a given name. Delegates to
        Lookups.has_table.

        name (unicode): Name of the table.
        RETURNS (bool): Whether a table of that name exists.
        """
        return self.has_table(name)

    def __len__(self):
        """RETURNS (int): The number of tables in the lookups."""
        return len(self._tables)

    @property
    def tables(self):
        """RETURNS (list): Names of all tables in the lookups."""
        return list(self._tables.keys())

    def add_table(self, name, data=SimpleFrozenDict()):
        """Add a new table to the lookups. Raises an error if the table exists.

        name (unicode): Unique name of table.
        data (dict): Optional data to add to the table.
        RETURNS (Table): The newly added table.
        """
        if name in self.tables:
            raise ValueError(Errors.E158.format(name=name))
        table = Table(name=name, data=data)
        self._tables[name] = table
        return table

    def get_table(self, name):
        """Get a table. Raises an error if the table doesn't exist.

        name (unicode): Name of the table.
        RETURNS (Table): The table.
        """
        if name not in self._tables:
            raise KeyError(Errors.E159.format(name=name, tables=self.tables))
        return self._tables[name]

    def remove_table(self, name):
        """Remove a table. Raises an error if the table doesn't exist.

        name (unicode): The name to remove.
        RETURNS (Table): The removed table.
        """
        if name not in self._tables:
            raise KeyError(Errors.E159.format(name=name, tables=self.tables))
        return self._tables.pop(name)

    def has_table(self, name):
        """Check if the lookups contain a table of a given name.

        name (unicode): Name of the table.
        RETURNS (bool): Whether a table of that name exists.
        """
        return name in self._tables

    def to_bytes(self, exclude=tuple(), **kwargs):
        """Serialize the lookups to a bytestring.

        exclude (list): String names of serialization fields to exclude.
        RETURNS (bytes): The serialized Lookups.
        """
        return srsly.msgpack_dumps(self._tables)

    def from_bytes(self, bytes_data, exclude=tuple(), **kwargs):
        """Load the lookups from a bytestring.

        exclude (list): String names of serialization fields to exclude.
        RETURNS (bytes): The loaded Lookups.
        """
        for key, value in srsly.msgpack_loads(bytes_data).items():
            self._tables[key] = Table(key)
            self._tables[key].update_raw(value)
        return self

    def to_disk(self, path, **kwargs):
        """Save the lookups to a directory as lookups.bin.

        path (unicode / Path): The file path.
        """
        if len(self._tables):
            path = ensure_path(path)
            filepath = path / "lookups.bin"
            srsly.write_msgpack(filepath, self._tables)

    def from_disk(self, path, **kwargs):
        """Load lookups from a directory containing a lookups.bin.

        path (unicode / Path): The file path.
        RETURNS (Lookups): The loaded lookups.
        """
        path = ensure_path(path)
        filepath = path / "lookups.bin"
        if filepath.exists():
            data = srsly.read_msgpack(filepath)
            for key, value in data.items():
                self._tables[key] = Table(key)
                self._tables[key].update_raw(value)
        return self


class Table(OrderedDict):
    """A table in the lookups. Subclass of builtin dict that implements a
    slightly more consistent and unified API. 

    Includes a Bloom filter to speed up missed lookups.
    """

    def __init__(self, name=None, data=None):
        """Initialize a new table.

        name (unicode): Optional table name for reference.
        data (dict): Initial data, used to hint Bloom Filter.
        RETURNS (Table): The newly created object.
        """
        self.name = name
        # assume a default size of 1M items
        size = 1E6
        if data and len(data) > 0:
            size = len(data)

        self.bloom = BloomFilter.from_error_rate(size)

        if data:
            self.update(data)

    def set(self, key, value): 
        """Set new key/value pair, where key is an integer. Same as
        table[key] = value.
        """
        self[key] = value

    def __setitem__(self, key, value):
        OrderedDict.__setitem__(self, key, value)
        self.bloom.add(key)

    def set_string(self, key, value):
        """Set new key/value pair, where key is a string to be hashed.
        """
        hkey = hash_string(key)
        self.set(hkey, value)

    def update(self, data):
        """Add entries in a dict-like to the table, where keys are strings to
        be hashed.
        """
        for key, val in data.items():
            self.set_string(key, val)

    def update_raw(self, data):
        """Add entries in a dict-like to the table, where keys are ints.
        """
        for key, val in data.items():
            self.set(key, val)

    def get(self, key, default=None):
        return OrderedDict.get(self, key, default)

    def get_string(self, key, default=None):
        hkey = hash_string(key)
        return OrderedDict.get(self, hkey, default)

    def __contains__(self, key):
        # This can give a false positive, so we need to check it after
        if key not in self.bloom: 
            return False
        return OrderedDict.__contains__(self, key)

    def contains_string(self, key):
        hkey = hash_string(key)
        return self.__contains__(hkey)

    def to_bytes(self):
        # TODO: serialize bloom too. For now just reconstruct it.
        return srsly.msgpack_dumps({'name': self.name, 'dict': dict(self.items())})

    def from_bytes(self, data):
        loaded = srsly.msgpack_loads(data)
        self.name = loaded['name']
        for key, val in loaded['dict'].items():
            self[key] = val
            self.bloom.add(key)

        return self

