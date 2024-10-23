from itertools import product
from time import sleep

ABC = '0123456789ab'
cnt = 0
for i in product(ABC, repeat=5):
    word = ''.join(i)
    count_more_8 = word.count('9') + word.count('a') + word.count('b')
    if word[0] != '0' and word.count('7') == 1 and count_more_8 < 4:
        print(word)
        cnt += 1
        # sleep(1)
print(cnt)

    # 10000