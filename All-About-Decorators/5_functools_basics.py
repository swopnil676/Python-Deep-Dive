import functools

    # Method 1
@functools.cache
def fibonacci(n): # 1 1 2 3 5 8 . .... .
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
        

    # Method 2
def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1

    cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    return cache[n]

print(fibonacci(40))