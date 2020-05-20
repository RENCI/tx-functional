import functools

to_python0 = lambda f: lambda: f(())

def from_python0(f):
    def fp02(a):
        if a == ():
            return f()
        else:
            raise RuntimeError(f"type error: the type of {a} is not unit")

to_python2 = lambda f: lambda a, b: f((a, b))

from_python2 = lambda f: lambda a: f(a[0], a[1])

to_python3 = lambda f: lambda a, b, c: f(((a, b), c))

from_python3 = lambda f: lambda a: f(a[0][0], a[0][1], a[1])

lassoc = lambda a: ((a[0], a[1][0]), a[1][1])

rassoc = lambda a: (a[0][0], (a[0][1], a[1]))

append = lambda l: lambda a : l + [a]

curry = lambda f: lambda a: lambda b: f((a, b))

uncurry = lambda f: lambda ab: f(ab[0])(ab[1])

foldl = lambda f: lambda a: lambda bs: functools.reduce(to_python2(uncurry(f)), bs, a)

def case_uncurried_uncurried_python(a,f,g):
    if isinstance(a, Left):
        return f(a.value)
    else:
        if isinstance(a, Right):
            return g(a.value)
        else:
            raise RuntimeError(f"cannot apply case to {a}")
    
case = curry(curry(from_python3(case_uncurried_uncurried_python)))

identity = lambda a: a


class monad_utils:
    def __init__(self, monad):
        self._pure = monad.pure

    @property
    def pure(self):
        return self._pure

    @property
    def bind(self):
        return lambda ma: lambda f: ma.bind(f)

    @property
    def fmap(self):
        return lambda f: lambda ma: ma.map(f)

    @property
    def liftA2(self):
        return lambda f: lambda ma: lambda mb: ma.map(f).ap(mb) 

    @property
    def sequence(self):
        return lambda ms: foldl(self.liftA2(append))(self.pure([]))(ms)


