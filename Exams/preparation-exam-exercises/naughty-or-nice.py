behaviors = {
    "Nice": [],
    "Naughty": []
}


def over_one_index(k, i):
    counter = 0
    for t in k:
        if t[0] == i:
            counter += 1
            name = t[0]
    if counter > 1:
        return True
    else:
        return False


def over_one_name(k, n):
    counter = 0
    for t in k:
        if t[1] == n:
            counter += 1
    if counter > 1:
        return True
    else:
        return False


def naughty_or_nice_list(kids, *args, **kwargs):
    for arg in args:
        split = arg.split("-")
        index, behavior = int(split[0]), split[1]
        if over_one_index(kids, index):
            continue
        for tu in kids:
            if tu[0] == index:
                behaviors[behavior].append(tu[1])
                kids.remove(tu)
                break

    for name, kwargs_behavior in kwargs.items():
        if over_one_name(kids, name):
            continue
        for tu in kids:
            if tu[1] == name:
                behaviors[kwargs_behavior].append(name)
                kids.remove(tu)
                break

    result = ""

    for key, value in behaviors.items():
        if value:
            result += f"{key}: {', '.join(value)}"
            result += "\n"

    names = []
    if kids:
        for k, v in kids:
            names.append(v)

        result += f"Not found: {', '.join(names)}"

    return result
