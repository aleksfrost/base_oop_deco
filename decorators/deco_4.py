
from decos import benchmark

from random import randint

def memo(func):
  """
  Декоратор, запоминающий результаты исполнения функции func, чьи аргументы args должны быть хешируемыми
  """
  cache = {}

  def fmemo(*args):
    n = args
    if n in cache:
        return cache[n]
    else:
        cache[n] = func(*args)
    return cache[n]

  fmemo.cache = cache
  return fmemo

@benchmark
def fib1(n):
    if n < 2:
        return n
    return fib1(n-2) + fib1(n-1)


@memo
@benchmark
def fib2(n):
    if n < 2:
        return n
    return fib2(n-2) + fib2(n-1)



print(fib1(10))
print(fib2(10))