from typing import Dict, Any
import functools
import copy

from ..errors import Errors


class Underscore:
    mutable_types = (dict, list, set)
    doc_extensions: Dict[Any, Any] = {}
    span_extensions: Dict[Any, Any] = {}
    token_extensions: Dict[Any, Any] = {}

    def __init__(self, extensions, obj, start=None, end=None, label=None, kb_id=None):
        object.__setattr__(self, "_extensions", extensions)
        object.__setattr__(self, "_obj", obj)
        # Assumption is that for doc values, _start and _end will both be None
        # Span will set non-None values for _start and _end
        # Token will have _start be non-None, _end be None
        # This lets us key everything into the doc.user_data dictionary,
        # (see _get_key), and lets us use a single Underscore class.
        object.__setattr__(self, "_doc", obj.doc)
        object.__setattr__(self, "_start", start)
        object.__setattr__(self, "_end", end)
        if label is not None or kb_id is not None:
            # It is reasonably safe to assume that if label and kb_id are None,
            # they were not passed to this function. Span.label and kb_id are
            # converted to 0 in Span's c-tor and setters if they are None
            object.__setattr__(self, "_label", label)
            object.__setattr__(self, "_kb_id", kb_id)

    def __dir__(self):
        # Hack to enable autocomplete on custom extensions
        extensions = list(self._extensions.keys())
        return ["set", "get", "has"] + extensions

    def __getattr__(self, name):
        if name not in self._extensions:
            raise AttributeError(Errors.E046.format(name=name))
        default, method, getter, setter = self._extensions[name]
        if getter is not None:
            return getter(self._obj)
        elif method is not None:
            method_partial = functools.partial(method, self._obj)
            # Hack to port over docstrings of the original function
            # See https://stackoverflow.com/q/27362727/6400719
            method_docstring = method.__doc__ or ""
            method_docstring_prefix = (
                "This method is a partial function and its first argument "
                "(the object it's called on) will be filled automatically. "
            )
            method_partial.__doc__ = method_docstring_prefix + method_docstring
            return method_partial
        else:
            key = self._get_key(name)
            if key in self._doc.user_data:
                return self._doc.user_data[key]
            elif isinstance(default, self.mutable_types):
                # Handle mutable default arguments (see #2581)
                new_default = copy.copy(default)
                self.__setattr__(name, new_default)
                return new_default
            return default

    def __setattr__(self, name, value):
        if name not in self._extensions:
            raise AttributeError(Errors.E047.format(name=name))
        default, method, getter, setter = self._extensions[name]
        if setter is not None:
            return setter(self._obj, value)
        else:
            self._doc.user_data[self._get_key(name)] = value

    def set(self, name, value):
        return self.__setattr__(name, value)

    def get(self, name):
        return self.__getattr__(name)

    def has(self, name):
        return name in self._extensions

    def _get_key(self, name):
        if hasattr(self, "_label") :
            return ("._.", name, self._start, self._end, self._label, self._kb_id)
        else :
            return ("._.", name, self._start, self._end)


    @staticmethod
    def _replace_keys(old_underscore, new_underscore):
        """
        This function is called by Span when its kb_id or label are re-assigned.
        It checks if any user_data is stored for this span and replaces the keys
        """
        for name in old_underscore._extensions :
            old_key = old_underscore._get_key(name)
            new_key = new_underscore._get_key(name)
            if old_key in old_underscore._doc.user_data and old_key != new_key:
                old_underscore._doc.user_data[new_key] = old_underscore._doc.user_data.pop(old_key)


    @classmethod
    def get_state(cls):
        return cls.token_extensions, cls.span_extensions, cls.doc_extensions

    @classmethod
    def load_state(cls, state):
        cls.token_extensions, cls.span_extensions, cls.doc_extensions = state


def get_ext_args(**kwargs):
    """Validate and convert arguments. Reused in Doc, Token and Span."""
    default = kwargs.get("default")
    getter = kwargs.get("getter")
    setter = kwargs.get("setter")
    method = kwargs.get("method")
    if getter is None and setter is not None:
        raise ValueError(Errors.E089)
    valid_opts = ("default" in kwargs, method is not None, getter is not None)
    nr_defined = sum(t is True for t in valid_opts)
    if nr_defined != 1:
        raise ValueError(Errors.E083.format(nr_defined=nr_defined))
    if setter is not None and not hasattr(setter, "__call__"):
        raise ValueError(Errors.E091.format(name="setter", value=repr(setter)))
    if getter is not None and not hasattr(getter, "__call__"):
        raise ValueError(Errors.E091.format(name="getter", value=repr(getter)))
    if method is not None and not hasattr(method, "__call__"):
        raise ValueError(Errors.E091.format(name="method", value=repr(method)))
    return (default, method, getter, setter)


def is_writable_attr(ext):
    """Check if an extension attribute is writable.
    ext (tuple): The (default, getter, setter, method) tuple available  via
        {Doc,Span,Token}.get_extension.
    RETURNS (bool): Whether the attribute is writable.
    """
    default, method, getter, setter = ext
    # Extension is writable if it has a setter (getter + setter), if it has a
    # default value (or, if its default value is none, none of the other values
    # should be set).
    if setter is not None or default is not None or all(e is None for e in ext):
        return True
    return False
