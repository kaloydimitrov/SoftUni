string = input().split("|")

matrix = []

for row in string:
    matrix.append(row.split())

for sub in matrix[::-1]:
    print(" ".join(sub), end=" ")

# --------------------------------------------------

num = int(input())

matrix = []

for _ in range(num):
    matrix.append([int(x) for x in input().split()])

command = input()

while command != "END":
    data = command.split()
    row, col, value = [int(x) for x in data[1:]]

    if row + 1 > 4 or col + 1 > 4 or col < 0 or row < 0:
        print("Invalid coordinates")
        command = input()
        continue

    if data[0] == "Add":
        matrix[row][col] += value
    elif data[0] == "Subtract":
        matrix[row][col] -= value

    command = input()

for row in matrix:
    print(" ".join([str(x) for x in row]))

# --------------------------------------------------

size = int(input())

matrix = []

for r in range(size):
    matrix.append(list(input()))


def any_left(val):
    val_of_val = val[0]
    res = val.count(val_of_val)
    if res == len(values):
        return False
    else:
        return True


removed_knights = 0

while True:
    knights = {}
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                row_n_col = f"{row} {col}"
                knights[row_n_col] = 0

                if 0 <= row + 1 < size and 0 <= col - 2 < size:
                    if matrix[row + 1][col - 2] == "K":
                        knights[row_n_col] += 1
                if 0 <= row + 2 < size and 0 <= col - 1 < size:
                    if matrix[row + 2][col - 1] == "K":
                        knights[row_n_col] += 1
                if 0 <= row + 1 < size and 0 <= col + 2 < size:
                    if matrix[row + 1][col + 2] == "K":
                        knights[row_n_col] += 1
                if 0 <= row + 2 < size and 0 <= col + 1 < size:
                    if matrix[row + 2][col + 1] == "K":
                        knights[row_n_col] += 1
                if 0 <= row - 2 < size and 0 <= col - 1 < size:
                    if matrix[row - 2][col - 1] == "K":
                        knights[row_n_col] += 1
                if 0 <= row - 1 < size and 0 <= col - 2 < size:
                    if matrix[row - 1][col - 2] == "K":
                        knights[row_n_col] += 1
                if 0 <= row - 2 < size and 0 <= col + 1 < size:
                    if matrix[row - 2][col + 1] == "K":
                        knights[row_n_col] += 1
                if 0 <= row - 1 < size and 0 <= col + 2 < size:
                    if matrix[row - 1][col + 2] == "K":
                        knights[row_n_col] += 1

    values = [x for x in knights.values()]
    if not any_left(values):
        break

    dangerous_knight = [int(x) for x in max(knights, key=knights.get).split()]
    matrix[dangerous_knight[0]][dangerous_knight[1]] = "0"
    removed_knights += 1

print(removed_knights)

# --------------------------------------------------

import math

size = int(input())

matrix = []

for _ in range(size):
    matrix.append(input().split(" "))

bunny_row = 0
bunny_col = 0

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "B":
            bunny_row = r
            bunny_col = c

up_down_left_right = {
    "up": lambda a, b: (a - 1, b),
    "down": lambda a, b: (a + 1, b),
    "left": lambda a, b: (a, b - 1),
    "right": lambda a, b: (a, b + 1)
}

c = bunny_row
d = bunny_col

all_actions = {
    "up": [],
    "down": [],
    "left": [],
    "right": []
}

biggest_key = ""
biggest_value = -math.inf

for action in up_down_left_right:
    current_sum = 0
    c, d = up_down_left_right[action](c, d)
    while 0 <= c < size and 0 <= d < size and matrix[c][d] != "X":
        current_sum += int(matrix[c][d])
        all_actions[action].append(f"[{c}, {d}]")
        c, d = up_down_left_right[action](c, d)

    if all_actions[action]:
        all_actions[action].append(current_sum)

    c = bunny_row
    d = bunny_col

    if current_sum > biggest_value and all_actions[action]:
        biggest_value = current_sum
        biggest_key = action

print(biggest_key)
for item in all_actions[biggest_key]:
    print(item)

# --------------------------------------------------


