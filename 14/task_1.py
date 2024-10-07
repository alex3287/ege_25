# перевод из любой СС в 10-ную
for x in range(5, 38):
    num_1 = int('144', x)
    num_2 = int('24', x)
    suma = int('201', x)
    if num_1 + num_2 == suma:
        print(x)