from math import sqrt

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

# Challenge accepted.
def intsum2():
    th_place = 1
    while True:
        yield int((th_place - 1) * (th_place / 2.0))
        th_place += 1

# Doubler
def doubler():
    current = 1
    while True:
        yield current
        current *= 2

# Fibonacci sequence
def fib():
    current = 1
    next = 1
    while True:
        yield current
        current, next = next, current + next

# Prime numbers
def prime():
    current = 2
    while True:
        yield current
        current += 1
        # If a number is determined to be prime, the while for checking
        # prime-ness ends, going back to the top of the infinite while loop,
        # yielding the current prime value.
        while notprime(current):
            current += 1

# Verify if a number is prime or not. As a soon as a number is
# determined to be non-prime, return True
def notprime(number):
    for div in xrange(2, int(sqrt(number)+1)):
        if number % div is 0:
            return True
