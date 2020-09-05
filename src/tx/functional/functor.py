from dataclasses import dataclass
from typing import TypeVar, Any, NamedTuple, Callable
from .utils import Arrow, flip, compose, curry

class Functor:
    def __init__(self, _map: Callable[[Arrow[Any, Any], Any], Any]):
        self._map = _map

    def map(self, f: Arrow[Any, Any], ma: Any) -> Any:
        return self._map(f, ma)


