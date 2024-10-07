ABC = '0123456789ABCDEFG'

for x in ABC:
    num_1 = f'9759{x}'
    num_2 = f'3{x}108'
    suma = int(num_1, 17) + int(num_2, 17)
    if suma % 11 == 0:
        print(x, suma // 11)