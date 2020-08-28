import functools
from typing import Callable, TypeVar, Tuple, List

S = TypeVar("S")

T = TypeVar("T")

U = TypeVar("U")

V = TypeVar("V")

Arrow = Callable[[S], T]

def to_python0(f: Arrow[Tuple[()], T]) ->  Callable[[], T]:
    return lambda: f(())

def from_python0(f: Callable[[], T]) -> Arrow[Tuple[()], T]:
    return lambda _: f()

def to_python2(f : Arrow[Tuple[S, T], U]) ->  Callable[[S, T], U]:
    return lambda a, b: f((a, b))

def from_python2(f : Callable[[S, T], U]) -> Arrow[Tuple[S, T], U]:
    return lambda a: f(a[0], a[1])

def to_python3(f : Arrow[Tuple[Tuple[S, T], U], V]) -> Callable[[S, T, U], V]:
    return lambda a, b, c: f(((a, b), c))

def from_python3(f : Callable[[S, T, U], V]) -> Arrow[Tuple[Tuple[S, T], U], V]:
    return lambda a: f(a[0][0], a[0][1], a[1])

def lassoc(a : Tuple[S, Tuple[T, U]]) -> Tuple[Tuple[S, T], U]:
    return ((a[0], a[1][0]), a[1][1])

def rassoc(a : Tuple[Tuple[S, T], U]) -> Tuple[S, Tuple[T, U]]:
    return (a[0][0], (a[0][1], a[1]))

def curry(f : Callable[[S, T], U]) -> Arrow[S, Arrow[T, U]]:
    return lambda a: lambda b: f(a, b)

def uncurry(f : Arrow[S, Arrow[T, U]]) -> Callable[[S, T], U]:
    return lambda a, b: f(a)(b)

def foldl(f : Callable[[S, T], S], a: S, bs: List[T]) ->  S:
    return functools.reduce(f, bs, a)

def foldr(f : Callable[[S, T], T], a: T, bs: List[S]) ->  T:
    return foldl(flip(f), a, reversed(bs))

def identity(a : T) -> T:
    return a

def const(a : S, b: T) -> S:
    return a

def flip(f : Callable[[S, T], U]) -> Callable[[T, S], U]:
    return lambda a, b: f(b, a)

def compose(f: Arrow[T, U], g: Arrow[S, T]) -> Arrow[S, U]:
    return lambda a: f(g(a))






