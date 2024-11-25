# +1 *2  win >= 77 s1=7  1<=s2<=69       19=>18  20=> 31 34

# task_19
# def F(s1, s2, pos):
#     if s1 + s2 >= 77 and pos == 2: return True
#     if s1 + s2 < 77 and pos == 2: return False
#     if s1 + s2 >= 77: return False
#
#     return F(s1+1, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+1, pos+1) or F(s1, s2*2, pos+1)

#task_20
# def F(s1, s2, pos):
#     if s1 + s2 >= 77 and pos == 3: return True
#     if s1 + s2 < 77 and pos == 3: return False
#     if s1 + s2 >= 77: return False
#
#     if pos % 2 == 1:
#         return F(s1+1, s2, pos+1) and F(s1*2, s2, pos+1) and F(s1, s2+1, pos+1) and F(s1, s2*2, pos+1)
#     return F(s1+1, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+1, pos+1) or F(s1, s2*2, pos+1)

#task_20
def F(s1, s2, pos):
    if s1 + s2 >= 77 and (pos == 2 or pos == 4): return True
    if s1 + s2 < 77 and pos == 4: return False
    if s1 + s2 >= 77: return False

    if pos % 2 == 0:
        return F(s1+1, s2, pos+1) and F(s1*2, s2, pos+1) and F(s1, s2+1, pos+1) and F(s1, s2*2, pos+1)
    return F(s1+1, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+1, pos+1) or F(s1, s2*2, pos+1)


for s2 in range(1, 70):
    if F(7, s2, 0):
        print(s2)
