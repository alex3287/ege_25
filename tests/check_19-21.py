# +1 *2 win >= 63 s1=5 1<=s2<=58
# task 19
# def F(s1, s2, pos):
#     if s1+s2 >= 63 and pos == 2: return True
#     if s1+s2 < 63 and pos == 2: return False
#     if s1+s2 >= 63: return False
#     return F(s1+1, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+1, pos+1) or F(s1, s2*2, pos+1)
# task 20
# def F(s1, s2, pos):
#     if s1+s2 >= 63 and pos == 3: return True
#     if s1+s2 < 63 and pos == 3: return False
#     if s1+s2 >= 63: return False
#     if pos % 2 == 1:
#         return F(s1+1, s2, pos+1) and F(s1*2, s2, pos+1) and F(s1, s2+1,pos+1) and F(s1, s2*2, pos+1)
#     return F(s1+1, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+1, pos+1) or F(s1, s2*2, pos+1)
# task 21
def F(s1, s2, pos):
    if s1+s2 >= 63 and (pos == 2 or pos == 4): return True
    if s1+s2 < 63 and pos == 4: return False
    if s1+s2 >= 63: return False
    if pos % 2 == 0:
        return F(s1+1, s2, pos+1) and F(s1*2, s2, pos+1) and F(s1, s2+1, pos+1) and F(s1, s2*2, pos+1)
    return F(s1+1, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+1, pos+1) or F(s1, s2*2, pos+1)

def F12(s1, s2, pos):
    if s1+s2 >= 63 and pos == 2: return True
    if s1+s2 < 63 and pos == 2: return False
    if s1+s2 >= 63: return False
    if pos % 2 == 0:
        return F(s1+1, s2, pos+1) and F(s1*2, s2, pos+1) and F(s1, s2+1, pos+1) and F(s1, s2*2, pos+1)
    return F(s1+1, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+1, pos+1) or F(s1, s2*2, pos+1)

for s2 in range(1, 59):
    if F12(5, s2, 0):
        print(s2)
print('*'*50)
# for s2 in range(1, 59):
#     if F1(5, s2, 0):
#         print(s2)