from autorepr import autorepr, autotext
from tx.functional.monad import Monad

class Either(Monad):
    @staticmethod
    def pure(value):
        return Right(value)

    
class Left(Either):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return type(self) is type(other) and self.value == other.value

    __repr__ = autorepr(["value"])
    __str__, __unicode__ = autotext("Left({self.value})")
    
    def bind(self, f):
        return self


class Right(Either):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return type(self) is type(other) and self.value == other.value

    __repr__ = autorepr(["value"])
    __str__, __unicode__ = autotext("Right({self.value})")

    def bind(self, f):
        return f(self.value)


    
