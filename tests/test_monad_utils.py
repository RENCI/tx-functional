from tx.functional.either import Left, Right, Either
from tx.functional.utils import monad_utils

def test_sequence():

    mu = monad_utils(Either)

    assert mu.sequence([Right(1), Right(2), Right(3)]) == Right([1,2,3])
    assert mu.sequence([Left(1), Right(2), Right(3)]) == Left(1)
