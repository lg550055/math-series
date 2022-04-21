def fib(n):
  ''' Returns the nth Fibonacci number starting from 0'''
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  return fib(n-1) + fib(n-2)

def lucas(n):
  ''' Returns the nth Lucas number starting from 0'''
  if n <= 0:
    return 2
  elif n == 1:
    return 1
  return lucas(n-1) + lucas(n-2)

def sum_series(n, v0=0, v1=1):
  ''' Returns the nth number in a series starting from 0'''
  if n <= 0:
    return v0
  elif n == 1:
    return v1
  return sum_series(n-1,v0,v1) + sum_series(n-2,v0,v1)
