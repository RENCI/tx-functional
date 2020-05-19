class Monad:
    def map(self, g):
        return self.bind(lambda a: self.pure(g(a)))
