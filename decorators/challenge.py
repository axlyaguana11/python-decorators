import functools

def memoize(func):
    """This is a memoization function."""
    cache = {}
    @functools.wraps(func)
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = func(*args)
            return cache[args]
    return decorated_function

#This decorates the function to use a cache! 
@memoize
def fib(n):
    """This is the sequence of Fibonacci."""
    if n ==0:
        return 0
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(10))
print(fib.__doc__)