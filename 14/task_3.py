def ten_to_q(number):
    result = ''
    while number:
        digit = number % 3
        result += str(digit)
        number //= 3
    return result[::-1]


number = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
count = 0
while number:
    if number % 25 == 0:
        count += 1
    number //= 25

print(count)