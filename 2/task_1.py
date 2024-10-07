print('x y z')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            F = (x or y) <= (y == z)
            if F == 0:
                print(x, y, z)
