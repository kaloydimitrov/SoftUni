s = set()
num = int(input())

for _ in range(num):
    s.add(input())

[print(x) for x in s]

# ------------------------------------------------

s1, s2 = [int(x) for x in input().split(" ")]

set1 = set()
set2 = set()

for i1 in range(s1):
    set1.add(int(input()))

for i2 in range(s2):
    set2.add(int(input()))

result = set1 & set2

[print(x) for x in result]

# ------------------------------------------------

chars = list(input())

chars_times = {}

for char in chars:
    if char not in chars_times.keys():
        chars_times[char] = 0
    chars_times[char] += 1

for key, value in sorted(chars_times.items()):
    print(f"{key}: {value} time/s")

# ------------------------------------------------

string = input()
all_elements = {}

for el in string:
    if el not in all_elements.keys():
        all_elements[el] = 0
    all_elements[el] += 1

for i in sorted(all_elements.keys()):
    print(f"{i}: {all_elements[i]} time/s")

# ------------------------------------------------

num = int(input())

all_items = {}

f_set = set()
s_set = set()

for _ in range(num):
    range1, range2 = input().split("-")
    f = [int(x) for x in range1.split(",")]
    s = [int(x) for x in range2.split(",")]

    for fi in range(f[0], f[1] + 1):
        f_set.add(fi)

    for si in range(s[0], s[1] + 1):
        s_set.add(si)

    r = [str(x) for x in list(f_set.intersection(s_set))]
    result = f"[{', '.join(r)}]"
    all_items[result] = len(r)

    f_set = set()
    s_set = set()

max_key = max(all_items, key=all_items.get)

print(f"Longest intersection is {max_key} with length {all_items[max_key]}")

# ------------------------------------------------

num = int(input())
current_sum = 0

odd_set = set()
even_set = set()

for time in range(1, num + 1):
    current_name = input()
    for char in current_name:
        current_sum += ord(char)

    current_sum = current_sum // time

    if current_sum % 2 == 0:
        even_set.add(current_sum)
    elif current_sum % 2 != 0:
        odd_set.add(current_sum)

    current_sum = 0

if sum(odd_set) == sum(even_set):
    result = odd_set.union(even_set)
elif sum(odd_set) > sum(even_set):
    result = odd_set - even_set
elif sum(even_set) > sum(odd_set):
    result = odd_set.symmetric_difference(even_set)

print(", ".join([str(x) for x in result]))
