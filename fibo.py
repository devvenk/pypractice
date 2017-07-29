#python 2.7.12

fib_cache = {}
from functools import Lru_cache

def fibonacci(n):

    if n in fib_cache:
        return fib_cache[n]

    if n == 1: return 1
    if n == 2: return 2

    if n > 2:
        val = fibonacci(n-1) + fibonacci(n-2)

    fib_cache[n] = val
    return val

@Lru_cache(max_size=1000)
def fibonacci_cache(n):
    if n == 1: return 1
    if n == 2: return 2

    if n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    for n in xrange(1, 1000):
        print n, " : ", fibonacci_cache(n)


if __name__ == '__main__':
    main()
