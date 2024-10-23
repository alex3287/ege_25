from itertools import product

ABC = 'ЕЛМРУ'
cnt = 0
k = 1
for i in product(ABC, repeat=4):
    word = ''.join(i)
    if word[0] == 'Л':
        print(k, word)
    k += 1
print(cnt)