# Sum of integers
# Yield current value, then at the following next()
# call, update values, and then yield updated sum value.
def intsum():
    current = 0
    sum = 0
    while True:
        yield sum
        current += 1
        sum += current


# Doubler
def doubler():
    current = 1
    while True:
        yield current
        current *= 2

# Fibonacci sequence
def fib():
    info = [1, 1]

    while True:
        yield info[0]
        info[0], info[1] = info[1], info[0] + info[1]


# Prime numbers
class prime(object):
    pass
