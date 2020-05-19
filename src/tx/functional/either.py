from tx.functional.monad import Monad

class Either(Monad):
    @staticmethod
    def pure(value):
        return Right(value)

    def bind(self, f):
        if isinstance(self, Left):
            return self
        else:
            return f(self)


class Left(Either):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return type(self) is type(other) and self.value == other.value
    

class Right(Either):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return type(self) is type(other) and self.value == other.value


    
