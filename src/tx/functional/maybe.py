from __future__ import annotations
from .monad import Monad
from .utils import identity, flip, to_python2, Arrow
from typing import Generic, TypeVar, Callable, Optional, Iterator, List
from abc import ABC
from dataclasses import dataclass

S = TypeVar("S")

T = TypeVar("T")

class Maybe(ABC, Generic[S]):
    def bind(self, f : Arrow[S, Maybe[T]]) -> Maybe[T]:
        return bind(self, f)

    def map(self, f : Arrow[S, T]) -> Maybe[T]:
        return maybe_monad.map(f, self)

    def rec(self, f : Arrow[S, T], g: T) -> T:
        return rec(self, f, g)

    def __iter__(self) -> Iterator[S]:
        empty_list : List[S] = []
        return iter(self.rec(lambda a: [a], empty_list))

@dataclass
class Just(Maybe[T]):
    value: T
    
@dataclass
class _Nothing(Maybe[T]):
    pass

Nothing = _Nothing[T]()

class Proxy(Generic[T]):
    pass

def rec(ma: Maybe[S], f: Arrow[S, T], g: T) ->  T:
    return f(ma.value) if isinstance(ma, Just) else g

def pure(value: T) -> Maybe[T]:
    return Just(value)

def bind(ma: Maybe[S], f: Arrow[S, Maybe[T]]) -> Maybe[T]:
    return rec(ma, f, Nothing)

maybe_functor = maybe_applicative = maybe_monad = Monad(pure, bind)

from_python = lambda a: Nothing if a is None else Just(a)
   
to_python = lambda a: a.rec(identity, None)

    
