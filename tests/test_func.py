from tx.functional.either import Left, Right
import pickle


def test_pickle_Left():
    pickle.dumps(Left(1))


def test_pickle_Right():
    pickle.dumps(Right(1))
    
