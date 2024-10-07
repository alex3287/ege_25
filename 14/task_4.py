def count_0(number):
    count = 0
    while number:
        if number % 5 == 0:
            count += 1
        number //= 5
    return count

for x in range(1, 2031):
    number = 5**150 + 5**100 - x
    if count_0(number) == 50:
        print(x, number)