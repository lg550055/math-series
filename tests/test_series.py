import pytest
from series import fib

def test_zero():
  actual = fib(0)
  expected = 0
  assert actual == expected

def test_one():
  actual = fib(1)
  expected = 1
  assert actual == expected

def test_two():
  actual = fib(2)
  expected = 1
  assert actual == expected

def test_three():
  actual = fib(3)
  expected = 2
  assert actual == expected

def test_seven():
  actual = fib(7)
  expected = 13
  assert actual == expected
