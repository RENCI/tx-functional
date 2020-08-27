from dataclasses import dataclass
from typing import TypeVar, Any, NamedTuple, Callable
from .utils import Arrow, flip, compose, curry
from .applicative import Applicative

class Monad(Applicative):
    def __init__(self, _pure: Arrow[Any, Any], _bind: Callable[[Any, Any], Any]):
        super().__init__(
            lambda f, ma: _bind(ma, lambda a: _pure(f(a))),
            _pure,
            lambda mf, ma: _bind(mf, lambda f: _bind(ma, lambda a: _pure(f(a))))
        )
        self._pure = _pure
        self._bind = _bind

    def pure(self, a: Any) -> Any:
        return self._pure(a)

    def bind(self, ma: Any, f: Arrow[Any, Any]) -> Any:
        return self._bind(ma, f)

