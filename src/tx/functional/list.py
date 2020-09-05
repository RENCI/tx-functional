from .traversable import Traversable

from typing import Generic, TypeVar, Callable, Any, List
from .functor import Functor
from .applicative import Applicative
from .utils import foldl, foldr, Arrow


S = TypeVar("S")

T = TypeVar("T")

def rec(ma: List[S], b: T, f: Callable[[S, T], T]) -> T:
    return foldr(f, b, ma)


def _map(f: Arrow[S, T], ma: List[S]) -> List[T]:
    return list(map(f, ma))


def append(l : List[T], a: T) -> List[T]:
    return l + [a]


def sequenceA(m: Applicative, ma: List[Any]) -> Any:
    return foldl(m.liftA2(append), m.pure([]), ma)


list_functor = Functor(_map)


def list_traversable(m: Applicative) -> Traversable:
    return Traversable(_map, lambda ma: sequenceA(m, ma))


