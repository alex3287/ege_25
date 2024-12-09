# 24 -> 46   +1  +1r
# def inc(number):
#     first, second = number // 10, number % 10
#     if first < 9:
#         first+=1
#     if second < 9:
#         second+=1
#     return first*10 + second

def inc(number):
    return number + 10 + (number % 10 != 9)

def F(start, finish):
    if start == finish:
        return 1
    if start > finish:
        return 0
    return F(start+1, finish) + F(inc(start), finish)


print(F(24, 46))