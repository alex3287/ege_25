from functools import lru_cache


@lru_cache()
def F(n):
    if n <= 1:
        return 3
    return F(n-1) + 2 * F(n-2) - 5

print(F(100))