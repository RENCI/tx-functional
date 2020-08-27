from tx.functional.either import either_monad, Left, Right
from tx.functional.list import list_traversable

def test_sequence():
    either = list_traversable(either_monad)
    assert either.sequence([Right(1), Right(2), Right(3)]) == Right([1,2,3])
    assert either.sequence([Left(1), Right(2), Right(3)]) == Left(1)
