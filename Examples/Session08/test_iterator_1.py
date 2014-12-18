import pytest

from iterator_1 import IterateMe_2


def test_def_start():
    numbers = [thing for thing in IterateMe_2(3, 10)]
    result = [thing for thing in xrange(3, 10)]
    
    assert numbers == result

def test_step_size():
    numbers = [thing for thing in IterateMe_2(2,20, 1)]
    result = [thing for thing in xrange(2, 20, 1)]

    assert numbers == result

def test_reset():
    me = IterateMe_2(2, 20)
    imp = xrange(2, 20)

    def iter_wrapper(iterator):
        def looper(stop=8):
            a = []
            for thing in iterator:
                if thing > stop: break
                a.append(thing)
            for thing in iterator:
                a.append(thing)
            return a
        return looper

    me = iter_wrapper(me)
    imp = iter_wrapper(imp)

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
    