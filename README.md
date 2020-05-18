[![Build Status](https://travis-ci.com/RENCI/tx-functional.svg?branch=master)](https://travis-ci.com/RENCI/tx-functional)

# tx-functional
Generic functional programming library for Python

# Either monad

```
Left(1)
Right(1)
Either.pure(1)
a.bind(lambda x: Left(1))
a.map(lambda x: 1)
```
