from itertools import product

ABC = 'КРОТ'
cnt = 0
for i in product(ABC, repeat=6):
    word = ''.join(i)
    if word.count('О') == 1:
        cnt += 1
        print(word)
print(cnt)