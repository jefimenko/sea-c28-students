# Sum of integers
class intsum(object):
    """
    Return a generator that produces the cumulative sum of integers.
    Start from 0, incrementing in steps of 1.
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
    pass

# Fibonacci sequence
class fib(object):
    pass

# Prime numbers
class prime(object):
    pass
