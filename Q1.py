import random


def print_random(n):
    i = 0
    while i <= n:
        x = random.randint(0, 255)
        print(f'{x:08b}')
        i += 1


y = int(input("Enter number: "))
print_random(y)
