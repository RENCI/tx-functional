from dataclasses import dataclass
from typing import TypeVar, Any, NamedTuple, Callable
from .utils import Arrow, flip, compose, curry
from .functor import Functor

class Applicative(Functor):
    def __init__(self, _map: Callable[[Arrow[Any, Any], Any], Any], _pure: Arrow[Any, Any], _ap: Callable[[Arrow[Any, Any], Any], Any]):
        super().__init__(_map)
        self._pure = _pure
        self._ap = _ap

    def pure(self, a: Any) -> Any:
        return self._pure(a)

    def ap(self, mf: Arrow[Any, Any], ma: Any) -> Any:
        return self._ap(mf, ma)

    def liftA2(self, f: Callable[[Any, Any], Any]) -> Callable[[Any, Any], Any]:
        return lambda ma, mb: self._ap(self._map(curry(f), ma), mb) 
