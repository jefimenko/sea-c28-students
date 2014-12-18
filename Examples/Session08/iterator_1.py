#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe_1(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """
    def __init__(self, stop=5):
        self.current = -1
        self.stop = stop
    def __iter__(self):
        return self
    def next(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration

class IterateMe_2(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """
    def __init__(self, start, stop, step=1):
        # Prevent invalid parameter input
        if not (isinstance(start, int)
                and isinstance(stop, int)
                and isinstance(step, int)):
            raise TypeError

        # Prevent step of size 0
        if not step:
            raise ValueError

        # Ensure valid range for positive step size
        if step > 0:
            if start > stop:
                self.stop = start
            else:
                self.stop = stop
        # Ensure valid range for negative step size
        else:
            if (start < stop):
                self.start = stop
            else:
                self.start = start
        self.step = step
        self.current = start - 1
    def __iter__(self):
        return self
    def next(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration



if __name__ == "__main__":

    print "first version"
    for i in IterateMe_1():
        print i

    print u'second version'
    it = IterateMe_2(2,20,2)
    for i in it:
        print i
        if i > 10: break
    # Check behaviour upon resuming iteration.
    print u'break'

    for i in it:
        print i
