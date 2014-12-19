# Sum of integers
class intsum(object):
    """
    Produces the cumulative sum of integers using intsum.next().
    Start from 0, adding incrementally larger numbers.
    """
    def __init__(self):
        self.current = 0
        self.sum = 0

    # Increment and sum values accordingly and return self.sum before addition
    # of current value.
    def next(self):
        self.current += 1
        self.sum += self.current
        return self.sum - self.current


# Doubler
class doubler(object):
    """
    Produce results of 2 raised to the power of n, where
    2^0 is defined as 1, and used as the first case.
    """
    def __init__(self):
        self.info = [1, 1]

    # Calculate result for next call while preserving and returning
    # current result
    def next(self):
        self.info[0], self.info[1] = self.info[1], self.info[1]*2
        return self.info[0]

# Fibonacci sequence
class fib(object):
    pass

# Prime numbers
class prime(object):
    pass
