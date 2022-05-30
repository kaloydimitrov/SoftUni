occurrences = {}

numbers = [float(x) for x in input().split()]

for number in numbers:
    if number not in occurrences:
        occurrences[number] = 0
    occurrences[number] += 1

for items in occurrences.items():
    print(f"{items[0]} - {items[1]} times")
