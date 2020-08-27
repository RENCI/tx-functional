[![Build Status](https://travis-ci.com/RENCI/tx-functional.svg?branch=master)](https://travis-ci.com/RENCI/tx-functional)

# tx-functional
Generic functional programming library for Python

The goal of this is
 * Close to Haskell.
 * Work with mypy
 * Pickleable

We choose functions in uncurried form because mypy doesn't support type variable that only appear in return type of a function signature.

## classes

### Functor

The `Functor` class is defined in `tx.functional.functor`.
It takes in a `_map` argument. A functor `F` is a higer-kinded type `* -> *`. 
A functor is defined by a `map` function
```
map: (S -> T, F[S]) -> F[T]
```

### Applicative

The `Applicative` class is defined in `tx.functional.applicative`.
It takes in `_map`, `_pure`, and `_ap`. An applicative `F` is a functor.
An applicative is defined by additional `pure` and `ap` functions
```
pure: S -> F[S]
ap: (F[S -> T], F[S]) -> F[T]
```

### Monad

The `Monad` class is defined in `tx.functional.monad`.
It takes in `_pure` and `_bind`. A monad `F` is an applicative and a functor.
A monad is defined by an additional `bind` function
```
bind: (F[S], S -> F[T]) -> F[T]
```

### Traversable

The `Traversable` class is defined in `tx.functional.traversable`.
It takes in `_sequenceA`. A traversable `F` is a functor. 
A traversable is defined by an additional `sequenceA` function
```
sequenceA: F[G[S]] -> G[F[S]]
```
where `G` is an applicative

## instances

### Maybe
`Maybe` is defined in `tx.functional.maybe`. It has two constructors, `Just` and `_Nothing`. An object `Nothing` is defined.

We should always use `== Nothing` to test equality and not `is Nothing`.

The `Functor` instance `maybe_functor`, `Applicative` instance `maybe_applicative`, and `Monad` instance `maybe_monad` are defined. 

```
Just(1)
Nothing
maybe_applicative.pure(1)
a.bind(lambda x: Nothing)
a.map(lambda x: 1)
```

### Either 
`Either` is defined in `tx.functional.either`.  It has two constructors, `Left` and `Right`. 

The `Functor` instance `either_functor`, `Applicative` instance `either_applicative`, and `Monad` instances `either_monad` are defined.

```
Left(1)
Right(1)
either_applicative.pure(1)
a.bind(lambda x: Left(1))
a.map(lambda x: 1)
```

### List
The python builtin types are used. The `Functor` instance `list_functor` and `Traversable` instance `list_traversable` are defined in `tx.functional.list`.

The `list_traversable` instance is a function that takes in an applicative.

```
list_traversable(maybe_applicative).sequenceA([Just(1)])
```
