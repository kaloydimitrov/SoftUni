occurrences = {}

numbers = [float(x) for x in input().split()]

for number in numbers:
    if number not in occurrences:
        occurrences[number] = 0
    occurrences[number] += 1

for items in occurrences.items():
    print(f"{items[0]} - {items[1]} times")

# ------------------------------------------------------------------------

num = int(input())

dic = {}

for _ in range(num):
    current = input().split()
    name = current[0]
    grade = float(current[1])

    if name not in dic:
        dic[name] = []

    dic[name].append(grade)

for n, g in dic.items():
    formatted = ' '.join(f"{x:.2f}" for x in g)
    print(f"{n} -> {formatted} (avg: {(sum(g) / len(g)):.2f})")

# ------------------------------------------------------------------------

s = set()

num = int(input())

for _ in range(num):
    s.add(input())

[print(x) for x in s]

# ------------------------------------------------------------------------

import sys

num = int(input())
s = set()

for _ in range(num):
    command, car = input().split(", ")
    if command == "IN":
        s.add(car)
    elif command == "OUT":
        s.remove(car)

    if not s:
        print("Parking Lot is Empty")
        sys.exit()

[print(x) for x in s]

# ------------------------------------------------------------------------

regs = set()
vips = set()

num = int(input())

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for _ in range(num):
    reservation_number = input()
    if reservation_number[0] in numbers:
        vips.add(reservation_number)
    else:
        regs.add(reservation_number)


command = input()

while command != "END":
    if command in vips:
        vips.remove(command)
    elif command in regs:
        regs.remove(command)

    command = input()

print(len(vips) + len(regs))

[print(x) for x in sorted(vips)]
[print(x) for x in sorted(regs)]
