import pytest

from iterator_1 import IterateMe_2


def test_def_start():
    numbers = [thing for thing in IterateMe_2(3, 10)]
    result = [thing for thing in xrange(3, 10)]
    
    assert numbers == result

def test_step_size():
    numbers = [thing for thing in IterateMe_2(2,20, 2)]
    result = [thing for thing in xrange(2, 20, 2)]

    assert numbers == result

def test_decreasing():
    numbers = [thing for thing in IterateMe_2(2, 20, -2)]
    result = [thing for thing in xrange(2, 20, -2)]

    assert numbers == result

def test_reset():

    def iter_wrapper(iterator):
        def looper(stop=8):
            a = []
            for thing in iterator:
                a.append(thing)
                if thing > stop: break
            for thing in iterator:
                a.append(thing)
            return a
        return looper

    me = iter_wrapper(IterateMe_2(2, 20))
    imp = iter_wrapper(xrange(2, 20))

    assert me() == imp()

def test_adjust_range():
    break_2 = IterateMe_2(10, 1)
    assert [thing for thing in break_2] == [thing for thing in xrange(10, 1)]
    break_2 = IterateMe_2(10, 1, -1)

def test_bad_step():
    with pytest.raises(ValueError):
        break_2 = IterateMe_2(1, 2, 0)

def test_bad_input_type():
    with pytest.raises(TypeError):
        break_2 = IterateMe_2(1, 2, .1)
    with pytest.raises(TypeError):
        break_2 = IterateMe_2(1, 2, 'asdf')
    with pytest.raises(TypeError):
        break_2 = IterateMe_2('asdf', 2)
    with pytest.raises(TypeError):
        break_2 = IterateMe_2(1, 'asdf', 2)
    