#!/usr/bin/env python

# Test the mathmatical series written as functions in series.py.

from series import fibonacci, lucas, sum_series

# Tests for Fibonacci series

def test_first_case_f():
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1

def test_later_case_f():
    assert fibonacci(3) == 1
    assert fibonacci(20) == 4181

def test_invalid_input_f():
    assert lucas(-13) is None

# Tests for Lucas Numbers

def test_first_case_l():
    assert lucas(1) == 2
    assert lucas(2) == 1

def test_later_case_l():
    assert lucas(3) == 3
    assert lucas(101) == 792070839848372253127

def test_invalid_input_l():
    assert lucas(-2) is None

# Tests for sum_series

def test_verify_fibonacci():
    assert sum_series(1) == 0
    assert sum_series(1, 0, 1) == 0
    assert sum_series(2) == 1
    assert sum_series(2, 0, 1) == 1
    assert sum_series(3) == 1
    assert sum_series(20) == 4181
    assert sum_series(20, 0, 1) == 4181

def test_verify_lucas():
    assert sum_series(1, 2, 1) == 2
    assert sum_series(2, 2, 1) == 1
    assert sum_series(3, 2, 1) == 3
    assert sum_series(101, 2, 1) == 792070839848372253127

def test_invalid_input_series():
    assert sum_series(0) is None