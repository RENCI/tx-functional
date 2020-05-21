from tx.functional.maybe import Maybe, Just, Nothing, maybe


def test_eq_on_Just():
    assert Just(1) == Just(1)


def test_ne_on_Just():
    assert Just(1) != Just(2)
    assert Just(1) != Nothing

    
def test_eq_on_Nothing():
    assert Nothing == Nothing

    
def test_ne_on_Nothing():
    assert Nothing != Just(1)


def test_bind_on_Just0():
    assert Just(1).bind(lambda x:x) == 1

    
def test_bind_on_Just():
    assert Just(1).bind(lambda x:Just(x+1)) == Just(2)

    
def test_bind_on_Nothing():
    assert Nothing.bind(lambda x:Just(1)) == Nothing


def test_pure():
    assert Maybe.pure(1) == Just(1)

    
def test_map_on_Just():
    assert Just(1).map(lambda x:2) == Just(2)

    
def test_map_on_Nothing():
    assert Nothing.map(lambda x:2) == Nothing


def test_maybe_to_python():
    assert maybe.to_python(Nothing) == None
    assert maybe.to_python(Just(1)) == 1


def test_maybe_from_python():
    assert maybe.from_python(None) == Nothing
    assert maybe.from_python(1) == Just(1)


def test_rec():
    assert Nothing.rec(lambda x:x+2, 3) == 3
    assert Just(2).rec(lambda x:x+2, 3) == 4


    
