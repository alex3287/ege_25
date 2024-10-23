from itertools import product

ABC = '0234567'
cnt = 0
for i in product(ABC, repeat=5):
    word = ''.join(i)
    if word[0] != '0' and len(set(word)) == 5:
        if all([(int(word[j]) + int(word[j+1])) % 2 != 0 for j in range(4)]):
            cnt += 1
            print(word)
print(cnt)