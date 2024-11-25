# -2 -5 //3  win <= 19  s >= 19        # 60, 61    62, 63, 65, 66
def F(s, pos):
    if s <= 19 and (pos == 2 or pos == 4): return True
    if s > 19 and pos == 4: return False
    if s <= 19: return False

    if pos % 2 == 0:
        return F(s-2, pos+1) and F(s-5, pos+1) and F(s//3, pos+1)
    return F(s-2, pos+1) or F(s-5, pos+1) or F(s//3, pos+1)


for s in range(20, 100):
    if F(s, 0):
        print(s)