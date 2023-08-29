# TODO: Decorators: Done
# TODO: *args, **kwargs: Done
# TODO: Error Handling
# TODO: Iterators and Generators

from datetime import datetime


def time_decorator(func):
    def wrapper():
        func()

        current_time = datetime.now().strftime("%H:%M:%S")
        print("Current Time: ", current_time)

    return wrapper


@time_decorator
def print_function():
    user_input = input('Enter meaningless text: ')
    print('Your text is:', user_input)


print_function()

print('\n------------------------------------------------------\n')


def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


args = ("Geeks", "for", "Geeks")
myFun(*args)
myFun('I', 'say', 'Yes')

print('++++++++-%-++++++++')

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)
myFun(arg1='I', arg2='say', arg3='Yes')

print('\n------------------------------------------------------\n')



