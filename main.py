# TODO: OOP: Done
# TODO: Decorators: Done
# TODO: *args, **kwargs: Done
# TODO: Slicing: Done
# TODO: Tuples and Sets: Done
# TODO: Getters and Setters: Done
# TODO: Iterators and Generators: Done
# TODO: Error Handling: Done
# TODO: Magic Methods
# TODO: Recursion (YouTube)
# TODO: Unittest
# Django Testing

from datetime import datetime


def time_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

        current_time = datetime.now().strftime("%H:%M:%S")
        print("Current Time:", current_time)

    return wrapper


@time_decorator
def print_function(additional_text):
    user_input = input('Enter meaningless text: ')
    print('Your text is:', user_input)
    print('Additional text is:', additional_text)


print_function('Text without any meaning')

print('\n------------------------------------------------------\n')


def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


args = ("Geeks", "for", "Geeks")
myFun(*args)
myFun('I', 'say', 'Yes')

print('\n')

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)
myFun(arg1='I', arg2='say', arg3='Yes')

print('++++++++-%-++++++++')


def myNewFun(arg1, *args, **kwargs):
    print(f"{arg1}: {' '.join(args)} | {', '.join([f'{key}: {value}' for key, value in kwargs.items()])}")


myNewFun('Something', 's1', 's2', 's3', isGood=True, isFine=True)

print('\n------------------------------------------------------\n')

word = 'Kaloyan'

print(word[
      # Removes the N chars from left to right
      1
      :
      # Keeps the N chars from left to right
      -1
      ])

print('\n------------------------------------------------------\n')


class Employee:
    promotion_percent = 1.25

    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def apply_promotion(self):
        self.salary *= self.promotion_percent

    @classmethod
    def new_promotion(cls, value):
        cls.promotion_percent = value


e1 = Employee('Stefan', 'Stefanov', 2200)
e2 = Employee('Peter', 'Dimitrov', 1900)

e1.promotion_percent = 2
Employee.promotion_percent = 1.5
e2.new_promotion(1.6)

print(Employee.promotion_percent)
print('First employee:', e1.promotion_percent)
print('Second employee:', e2.promotion_percent)

print('\n------------------------------------------------------\n')


class Person:
    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError('Cannot be less than 0!')
        elif value > 120:
            raise ValueError('Cannot be higher than 120!')

        self.__age = value

    def __add__(self, other):
        return self.age + other.age


p1 = Person()
p1.age = 20
print(p1.age)
print(p1.__dict__)

p2 = Person(44)

print(p1 + p2)

print('\n------------------------------------------------------\n')


class Human:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        # Just to showcase that naming doesn't matter
        return self.whatever

    @name.setter
    def name(self, value):
        if value.isdigit():
            raise ValueError('Name cannot include digits!')

        # Just to showcase that naming doesn't matter
        self.whatever = value

    def __str__(self):
        return f"Name: {self.name}"


h1 = Human('Unifri')
print(h1)
print(h1.__dict__)

print('\n------------------------------------------------------\n')


class Animal:
    tricks = []

    def __init__(self, name=None):
        self.name = name


a1 = Animal('Salami')
a2 = Animal('Mitko')

# Mutable
a1.tricks.append('roll over')

print(a1.tricks)
print(a2.tricks)


class Animal:
    tricks = ()

    def __init__(self, name=None):
        self.name = name


a1 = Animal('Salami')
a2 = Animal('Mitko')

# Immutable
a1.tricks = ('roll over', 'make a jump')

print(a1.tricks)
print(a2.tricks)

print('\n------------------------------------------------------\n')

try:
    print(int(input('Enter a number: ')))
except ValueError as error:
    print(f"That's not a number: {error}")

print('\n------------------------------------------------------\n')


class Range:
    def __init__(self, end_num):
        self.end_num = end_num

    def __iter__(self):
        self.start_num = -1
        return self

    def __next__(self):
        self.start_num += 1

        if self.start_num >= self.end_num:
            raise StopIteration

        return self.start_num


for i in Range(10):
    print(i)

print('\n------------------------------------------------------\n')


def mygen():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30


for i in mygen():
    print(i)
