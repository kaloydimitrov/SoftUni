numbers = [int(x) for x in input().split()]


def sort_numbers(*args):
    negatives = 0
    positives = 0
    for number in args:
        if number < 0:
            negatives += number
        else:
            positives += number

    return positives, negatives


positive_sum, negative_sum = sort_numbers(*numbers)

print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")


# -----------------------------------------------------------------------

def kwargs_length(**kwargs):
    return len(kwargs)


# -----------------------------------------------------------------------

def even_odd(*args):
    evens = []
    odds = []
    type = args[-1]

    for num in args:
        if num == "even" or num == "odd":
            break
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    if type == "even":
        return evens
    else:
        return odds


# -----------------------------------------------------------------------

d = {}


def even_odd_filter(**kwargs):
    for even_or_odd, values in kwargs.items():
        if even_or_odd == "even":
            result = [x for x in values if x % 2 == 0]
            if result:
                d[even_or_odd] = result
        else:
            result = [x for x in values if x % 2 != 0]
            if result:
                d[even_or_odd] = result

    return dict(sorted(d.items(), key=lambda x: len(x[1]), reverse=True))


# -----------------------------------------------------------------------

def concatenate(*args, **kwargs):
    line = "".join(list(args))
    for old_word, new_word in kwargs.items():
        line = line.replace(old_word, new_word)

    return line


# -----------------------------------------------------------------------

def func_executor(*args):
    results = ""
    for func, func_params in args:
        result = f"{func.__name__} - {func(*func_params)}"
        results += result + "\n"

    return results


# -----------------------------------------------------------------------

def grocery_store(**kwargs):
    result = ""
    r = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    for key, value in r:
        current_result = f"{key}: {value}"
        result += current_result + "\n"

    return result


# -----------------------------------------------------------------------

def age_assignment(*args, **kwargs):
    result = {}
    for key, value in kwargs.items():
        for name in args:
            if name[0] == key:
                result[name] = value

    sort = sorted(result.items(), key=lambda x: x[0])

    result = ""

    for name, age in sort:
        current_result = f"{name} is {age} years old."
        result += current_result + "\n"

    return result
