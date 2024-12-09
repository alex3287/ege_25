def F(start, finish):
    if start == finish:
        return 1
    if start > finish:
        return 0
    return F(start+1, finish) + F(start+2, finish) + F(start*2, finish)


print(F(3, 10) * F(10, 13))