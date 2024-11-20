# 5! = 1*2*3*4*5
# F(n) = 1, if n == 1
# F(n) = n * F(n-1)
# F(2) = 2 * F(2-1) = 2
# F(3) = 3 * F(3-1) = 6

def F(n):
    if n == 1:
        return 1
    return n * F(n-1)


print(F(10))
