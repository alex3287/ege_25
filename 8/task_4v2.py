from itertools import product

ABC = '0234567'
cnt = 0
for i in product(ABC, repeat=5):
    word = ''.join(i)
    if word[0] != '0' and len(set(word)) == 5:
        word = word.replace('0','2').replace('4', '2').replace('6', '2')
        word = word.replace('5','3').replace('7', '3')
        if '22' not in word and '33' not in word:
            cnt += 1
            print(word)
print(cnt)