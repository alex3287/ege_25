ABC = 'ЛЕТО'

cnt = 0
for a in ABC:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                word = a + b + c + d
                if word[0] in 'ЛТ':
                    cnt += 1
                    print(word)
print(cnt)