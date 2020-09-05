from tx.functional.list import list_traversable, rec, list_functor
from tx.functional.maybe import maybe_monad, maybe_applicative, Just, Nothing
import pytest

@pytest.fixture
def list_traversable_maybe_applicative():
    return list_traversable(maybe_applicative)


@pytest.fixture
def list_traversable_maybe_monad():
    return list_traversable(maybe_monad)


def test_sequence(list_traversable_maybe_monad):
    assert list_traversable_maybe_monad.sequence([Just(1), Nothing]) == Nothing

    
def test_sequence2(list_traversable_maybe_monad):
    assert list_traversable_maybe_monad.sequence([Just(1)]) == Just([1])


def test_mapM(list_traversable_maybe_monad):
    assert list_traversable_maybe_monad.mapM(lambda a: Just(1) if a else Nothing, [True, False]) == Nothing
    

def test_mapM2(list_traversable_maybe_monad):
    assert list_traversable_maybe_monad.mapM(lambda a: Just(1) if a else Nothing, [True]) == Just([1])
    

def test_sequenceA(list_traversable_maybe_applicative):
    assert list_traversable_maybe_applicative.sequenceA([Just(1), Nothing]) == Nothing

    
def test_sequenceA2(list_traversable_maybe_applicative):
    assert list_traversable_maybe_applicative.sequenceA([Just(1)]) == Just([1])


def test_traverse(list_traversable_maybe_applicative):
    assert list_traversable_maybe_applicative.traverse(lambda a: Just(1) if a else Nothing, [True, False]) == Nothing
    

def test_traverse2(list_traversable_maybe_applicative):
    assert list_traversable_maybe_applicative.traverse(lambda a: Just(1) if a else Nothing, [True]) == Just([1])

    
def test_list_rec():
    assert rec([1,2,3], 0, lambda x,y : x+y) == 6


def test_list_map():
    assert list_functor.map(lambda x:1-x, [1]) == [0]
