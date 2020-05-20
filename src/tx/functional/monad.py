class Monad:
    def map(self, g):
        return self.bind(lambda a: self.pure(g(a)))

    def ap(self, a):
        return self.bind(lambda f: a.map(f))
