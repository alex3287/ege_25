# 3 -> 20  +1 *2

def F(start, finish, com=''):
    if start == finish and com[-2] == '1':
        print(com)
        return 1
    if start > finish:
        return 0
    return F(start+1, finish, com+'1') + F(start*2, finish, com+'2')

print('answer', F(3, 20))
