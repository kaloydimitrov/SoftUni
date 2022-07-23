from functools import reduce


class Calculator:
    @staticmethod
    def add(*args):
        return reduce((lambda a, b: a + b), args)

    @staticmethod
    def multiply(*args):
        return reduce((lambda a, b: a * b), args)

    @staticmethod
    def divide(*args):
        return reduce((lambda a, b: a / b), args)

    @staticmethod
    def subtract(*args):
        return reduce((lambda a, b: a - b), args)

# --------------------------------------------------------------------------

class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, item_name):
        if self.capacity <= sum(self.items.values()):
            return "Not enough capacity in the shop"
        if item_name not in self.items.keys():
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name, amount):
        if item_name in self.items.keys() and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                self.items.pop(item_name)
            return f"{amount} {item_name} removed from the shop"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

# --------------------------------------------------------------------------


import math


def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in roman:
            num += roman[s[i:i + 2]]
            i += 2
        else:
            num += roman[s[i]]
            i += 1
    return num


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value: str):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(math.floor(float(float_value)))

    @classmethod
    def from_roman(cls, value: str):
        return cls(roman_to_int(value))

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        return cls(int(value))
