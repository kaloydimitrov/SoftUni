calculations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'divide': lambda x, y: x / y,
    'multiply': lambda x, y: x * y
}

print(calculations['add'](2, 2))
print(calculations['subtract'](2, 2))
print(calculations['divide'](2, 2))
print(calculations['multiply'](2, 2))

print('---------------------------------------------------------------------------------------')

import time
import math


def calculate_time(func):
    def inner1(*args, **kwargs):
        begin = time.time()

        func(*args, **kwargs)

        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1


@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))


factorial(10)

print('---------------------------------------------------------------------------------------')

print("yes", "no", "yes")

print("yes", end="\n\n")
print("no", end="\n\n")
print("yes", end="\n\n")

print('---------------------------------------------------------------------------------------')


def make_order(price, *args, **kwargs):
    print(price, end='; ')
    [print(item, end=' ') for item in args]

    for key, value in kwargs.items():
        if key == 'is_active':
            print(f"\nActive: {value}")
        elif key == 'is_offer':
            print(f"\nOffer: {value}")


make_order(67, 'Jonathan White - T-shirt', 'Armani - Shorts', 'Rolex g255 - Watch', is_active=True, is_offer=True, teea=True)
