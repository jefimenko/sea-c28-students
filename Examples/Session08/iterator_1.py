#!/usr/bin/env python

import copy

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

    returns the sequence of numbers from  start to stop-1
    """
    def __init__(self, start, stop, step=1):
        # Prevent invalid parameter input
        if not (isinstance(start, int)
                and isinstance(stop, int)
                and isinstance(step, int)):
            raise TypeError(u'All parameters given must be of type int')

        # Prevent step of size 0
        if not step:
            raise ValueError(u'Step size must be a non-zero int.')

        # Ensure valid range for positive step size
        self.start = start
        if step > 0:
            if (start > stop):
                self.stop = start
            else:
                self.stop = stop
        # Ensure valid range for negative step size
        else:
            if (start < stop):
                self.stop = start
            else:
                self.stop = stop
        self.step = step
        self.current = start - step

    def __iter__(self):
        # FOR HOMEWORK: create behavior similar to xrange() by passing
        # a copy to be iterated through. At the expense of more memory
        # usage, each attempt to iterate through an IterateMe_2 object
        # begins at the start of a copy of a given instance, instead of
        # where the last .next() call left off
        return copy.copy(self)

    def next(self):
        self.current += self.step
        return self.check_to_keep_going()

    # For incrementing iterations, test to see if strictly less than 
    # stop value, for decrementing iterations, test to see if strictly 
    # greater than stop value, and return value to continue iteration,
    # otherwise raise StopIteration
    def check_to_keep_going(self):
        if self.step > 0:
            if self.current < self.stop:
                pass
            else:
                raise StopIteration
        else:
            if self.current > self.stop:
                pass
            else:
                raise StopIteration
        return self.current

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
