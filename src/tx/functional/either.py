from __future__ import annotations
from .monad import Monad
from .utils import const, flip, to_python2, Arrow

from typing import Generic, TypeVar, Callable, Iterator, List, cast
from abc import ABC
from dataclasses import dataclass

T = TypeVar("T")

S = TypeVar("S")

U = TypeVar("U")

class Either(ABC, Generic[S, T]):
    def bind(self, f : Arrow[T, Either[S, U]]) -> Either[S, U]:
        return bind(self, f)

    def map(self, f : Arrow[T, U]) -> Either[S, U]:
        return either_monad.map(f, self)

    def rec(self, f : Arrow[S, U], g: Arrow[T, U]) -> U:
        return rec(self, f, g)

    def __iter__(self) -> Iterator[T]:
        empty_list : List[T] = []
        return iter(self.rec(lambda _: empty_list, lambda a: [a]))


@dataclass
class Left(Either[S, T]):
    value: S
    

@dataclass
class Right(Either[S, T]):
    value: T


def rec(ma: Either[S, T], f: Arrow[S, U], g: Arrow[T, U]) -> U:
    return f(ma.value) if isinstance(ma, Left) else g(cast(Right[S, T], ma).value)


def pure(a: T) -> Either[S, T]:
    return Right(a)


def bind(ma: Either[S, T], f: Arrow[T, Either[S, U]]) -> Either[S, U]:
    return rec(ma, lambda b: Left(b), f)

either_functor = either_applicative = either_monad = Monad(pure, bind)


    
