# 38 -> 2 (16)   -2  //2
def F(start, finish):
    if start == finish:
        return 1
    if start < finish:
        return 0
    return F(start-2, finish) + F(start//2, finish)


print(F(38, 16) * F(16, 2))