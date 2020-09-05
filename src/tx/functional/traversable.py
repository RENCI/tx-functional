from dataclasses import dataclass
from typing import Generic, TypeVar, Callable, Any, NamedTuple
from .utils import Arrow
from .functor import Functor

class Traversable(Functor):
    def __init__(self, _map: Callable[[Arrow[Any, Any], Any], Any], _sequenceA: Arrow[Any, Any]):
        super().__init__(_map)
        self._sequenceA = _sequenceA

    def sequenceA(self, ma: Any) -> Any:
        return self._sequenceA(ma)

    def traverse(self, g: Arrow[Any, Any], ma: Any) -> Any:
        return self._sequenceA(self.map(g, ma))

    def sequence(self, ma: Any) -> Any:
        return self.sequenceA(ma)

    def mapM(self, g: Arrow[Any, Any], ma: Any) -> Any:
        return self.traverse(g, ma)


