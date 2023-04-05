from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#In this example, the fibonacci function is decorated with lru_cache.
#  The maxsize argument is set to None, 
# which means that there is no limit to the number of results that can be cached.

#Now, when the fibonacci function is called with a particular input,
#  the result will be cached. If the function is called again with the same input,
#  the cached result will be returned immediately instead of recomputing the result