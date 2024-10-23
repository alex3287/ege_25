from itertools import product

ABC = 'ЛЕТО'
cnt = 0
for i in product(ABC, repeat=4):
    word = ''.join(i)
    if word[0] in 'ЛТ':
        cnt += 1
        print(word)
print(cnt)