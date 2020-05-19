from tx.functional.monad import Monad

class Either(Monad):
    @staticmethod
    def pure(value):
        return Right(value)

    def bind(self, f):
        if isinstance(self.value, Left):
            return self
        else:
            return f(self.value)


class Left(Either):
    def __init__(self, value):
        self.value = value


class Right(Either):
    def __init__(self, value):
        self.value = value
