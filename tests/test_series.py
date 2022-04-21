import pytest
from math_series.series import fib, lucas, sum_series

def test_fzero():
  actual = fib(0)
  expected = 0
  assert actual == expected

def test_fone():
  actual = fib(1)
  expected = 1
  assert actual == expected

def test_ftwo():
  actual = fib(2)
  expected = 1
  assert actual == expected

def test_fthree():
  actual = fib(3)
  expected = 2
  assert actual == expected

def test_fseven():
  actual = fib(7)
  expected = 13
  assert actual == expected

def test_lzero():
  actual = lucas(0)
  expected = 2
  assert actual == expected

def test_lone():
  actual = lucas(1)
  expected = 1
  assert actual == expected

def test_ltwo():
  actual = lucas(2)
  expected = 3
  assert actual == expected

def test_lthree():
  actual = lucas(3)
  expected = 4
  assert actual == expected

def test_lseven():
  actual = lucas(7)
  expected = 29
  assert actual == expected

def test_ssfzero():
  actual = sum_series(0)
  expected = 0
  assert actual == expected

def test_ssfone():
  actual = sum_series(1)
  expected = 1
  assert actual == expected

def test_ssftwo():
  actual = sum_series(2)
  expected = 1
  assert actual == expected

def test_ssfthree():
  actual = sum_series(3)
  expected = 2
  assert actual == expected

def test_ssfseven():
  actual = sum_series(7)
  expected = 13
  assert actual == expected

def test_sslzero():
  actual = sum_series(0,2,1)
  expected = 2
  assert actual == expected

def test_sslone():
  actual = sum_series(1,2,1)
  expected = 1
  assert actual == expected

def test_ssltwo():
  actual = sum_series(2,2,1)
  expected = 3
  assert actual == expected

def test_sslthree():
  actual = sum_series(3,2,1)
  expected = 4
  assert actual == expected

def test_sslseven():
  actual = sum_series(7,2,1)
  expected = 29
  assert actual == expected
