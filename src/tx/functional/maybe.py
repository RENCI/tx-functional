from autorepr import autorepr, autotext
from tx.functional.monad import Monad
from tx.functional.utils import identity, monad_utils

class Maybe(Monad):
    @staticmethod
    def pure(value):
        return Just(value)

class Just(Maybe):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return type(self) is type(other) and self.value == other.value

    __repr__ = autorepr(["value"])
    __str__, __unicode__ = autotext("Just({self.value})")
    
    def bind(self, f):
        return f(self.value)

    def rec(self,f,g):
        return f(self.value)

    
class _Nothing(Maybe):
    def __init__(self):
        pass

    def __eq__(self, other):
        return type(self) is type(other)

    __repr__ = autorepr([])
    __str__, __unicode__ = autotext("Nothing")

    def bind(self, f):
        return self

    def rec(self,f,g):
        return g

    
Nothing = _Nothing()

maybe = monad_utils(Maybe)

maybe.from_python = lambda a: Nothing if a is None else Just(a)
    
maybe.to_python = lambda a: a.rec(identity, None)

    
