def F(n):
    if n <= 1:
        return 3
    return F(n-1) + 2 * F(n-2) - 5


print(F(10))