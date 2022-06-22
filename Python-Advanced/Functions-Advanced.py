def multiply(*args):
    r = 1
    for n in args:
        r *= n
    return r


# --------------------------------------------------------------------------

def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"


# --------------------------------------------------------------------------

def sorting_cheeses(**kwargs):
    sort = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for name, numbers in sort:
        result += name + "\n"
        sort_numbers = sorted(numbers, reverse=True)
        for number in sort_numbers:
            result += str(number) + "\n"
    return result

# --------------------------------------------------------------------------


