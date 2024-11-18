# 5! = 1*2*3*4*5
from sys import setrecursionlimit


setrecursionlimit(1020)
def factorial(number):
    if number < 2:
        return 1
    return number * factorial(number-1)

print(factorial(1000))