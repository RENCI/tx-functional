from tx.functional.either import Either, Left, Right
import pickle


def test_pickle_Left():
    pickle.dumps(Left(1))


def test_pickle_Right():
    pickle.dumps(Right(1))


def test_eq_on_Left():
    assert Left(1) == Left(1)


def test_ne_on_Left():
    assert Left(1) != Left(2)
    assert Left(1) != Right(1)

    
def test_eq_on_Right():
    assert Right(1) == Right(1)

    
def test_ne_on_Right():
    assert Right(1) != Right(2)
    assert Right(1) != Left(1)


def test_bind_on_Right0():
    assert Right(1).bind(lambda x:x) == 1

    
def test_bind_on_Right():
    assert Right(1).bind(lambda x:Right(x+1)) == Right(2)

    
def test_bind_on_Left():
    assert Left(1).bind(lambda x:Right(2)) == Left(1)


def test_pure():
    assert Either.pure(1) == Right(1)

    
def test_map_on_Right():
    assert Right(1).map(lambda x:2) == Right(2)

    
def test_map_on_Left():
    assert Left(1).map(lambda x:2) == Left(1)

    
def test_rec():
    assert Left(1).rec(lambda x:x, lambda x:x+1) == 1
    assert Right(2).rec(lambda x:x+1, lambda x:x) == 2
    
