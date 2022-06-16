a = int(input())

matrix = []

for _ in range(a):
    matrix.append([int(x) for x in input().split(", ")])

pr_sum = []
sc_sum = []

for index in range(a):
    pr_sum.append(matrix[index][index])
    sc_sum.append(matrix[index][-(index + 1)])

print(f"Primary diagonal: {', '.join([str(x) for x in pr_sum])}. Sum: {sum(pr_sum)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in sc_sum])}. Sum: {sum(sc_sum)}")

# ------------------------------------------------------------------------------------------

a = int(input())

matrix = []

for _ in range(a):
    matrix.append([int(x) for x in input().split(" ")])

pr_sum = []
sc_sum = []

for index in range(a):
    pr_sum.append(matrix[index][index])
    sc_sum.append(matrix[index][-(index + 1)])

print(abs(sum(pr_sum) - sum(sc_sum)))

# ------------------------------------------------------------------------------------------

rows, cols = [int(x) for x in input().split(" ")]

matrix = []

for _ in range(rows):
    matrix.append(input().split(" "))


def are_equal(items):
    item = items[0]
    count = items.count(item)
    if count == len(items):
        return True
    else:
        return False


count_of_squares = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        current_square = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]
        result = are_equal(current_square)
        if result:
            count_of_squares += 1

print(count_of_squares)

# ------------------------------------------------------------------------------------------

r, c = [int(x) for x in input().split(" ")]

matrix = []

for _ in range(r):
    matrix.append([int(x) for x in input().split(" ")])

biggest_square = -20
biggest_row = 0
biggest_col = 0

for row in range(r - 2):
    for col in range(c - 2):
        square = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + matrix[row + 1][col] + \
                 matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + matrix[row + 2][col] + matrix[row + 2][col + 1] + \
                 matrix[row + 2][col + 2]
        if square > biggest_square:
            biggest_square = square
            biggest_row = row
            biggest_col = col

print(f"Sum = {biggest_square}")
print(
    f"{matrix[biggest_row][biggest_col]} {matrix[biggest_row][biggest_col + 1]} {matrix[biggest_row][biggest_col + 2]}")
print(
    f"{matrix[biggest_row + 1][biggest_col]} {matrix[biggest_row + 1][biggest_col + 1]} {matrix[biggest_row + 1][biggest_col + 2]}")
print(
    f"{matrix[biggest_row + 2][biggest_col]} {matrix[biggest_row + 2][biggest_col + 1]} {matrix[biggest_row + 2][biggest_col + 2]}")

# ------------------------------------------------------------------------------------------

rows, cols = [int(x) for x in input().split(" ")]

for r in range(rows):
    first_symbol = chr(97 + r)
    for c in range(cols):
        second_symbol = chr(97 + r + c)
        print(f"{first_symbol}{second_symbol}{first_symbol}", end=" ")

    print()

# ------------------------------------------------------------------------------------------

r, c = [int(x) for x in input().split(" ")]

matrix = []

for _ in range(r):
    matrix.append(input().split(" "))

command = input()

while command != "END":
    data = command.split()
    if len(data) != 5 or data[0] != "swap":
        print("Invalid input!")
        command = input()
        continue

    row1, col1, row2, col2 = [int(x) for x in data[1:]]

    if r > row1 >= 0 and r > row2 >= 0 and c > col1 >= 0 and c > col2 >= 0:
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    else:
        print("Invalid input!")
        command = input()
        continue

    for row in matrix:
        print(" ".join([str(x) for x in row]))

    command = input()

# ------------------------------------------------------------------------------------------

from collections import deque

rows, cols = [int(x) for x in input().split(" ")]

matrix = []

for r in range(rows):
    matrix.append([])
    for _ in range(cols):
        matrix[r].append(0)

string = input()
string1 = deque(list(string))

for row in range(rows):
    for col in range(cols):
        current_symbol = string1.popleft()
        if len(string1) == 0:
            string1 = deque(list(string))

        if row % 2 != 0:
            matrix[row][-(1 + col)] = current_symbol
        else:
            matrix[row][col] = current_symbol

for print_row in matrix:
    print("".join(print_row))

# ------------------------------------------------------------------------------------------

size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

bombs_rows_cords = input().split()
dead_cells = []


def cell_changer(r, c, v):
    if 0 <= r < size and 0 <= c < size and f"{r} {c}" not in dead_cells:
        matrix[r][c] -= v
        if matrix[r][c] <= 0:
            dead_cells.append(f"{r} {c}")


for cord in bombs_rows_cords:
    row, col = (int(x) for x in cord.split(","))
    dead_cells.append(f"{row} {col}")
    value = matrix[row][col]

    cell_changer(row - 1, col, value)
    cell_changer(row + 1, col, value)
    cell_changer(row, col - 1, value)
    cell_changer(row, col + 1, value)
    cell_changer(row - 1, col - 1, value)
    cell_changer(row - 1, col + 1, value)
    cell_changer(row + 1, col - 1, value)
    cell_changer(row + 1, col + 1, value)

    matrix[row][col] = 0

alive_cells = 0
alive_cells_sum = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] > 0:
            alive_cells += 1
            alive_cells_sum += matrix[row][col]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_cells_sum}")
[print(" ".join([str(y) for y in x])) for x in matrix]

# ------------------------------------------------------------------------------------------

import sys

size = int(input())
directions = input().split()

matrix = []

miner_row = 0
miner_col = 0

c_count = 0
c_collected = 0

for r in range(size):
    line = input().split()
    matrix.append(line)
    for c in range(size):
        if matrix[r][c] == "s":
            miner_row = r
            miner_col = c
        elif matrix[r][c] == "c":
            c_count += 1

up_down_left_right = {
    "up": lambda a, b: (a - 1, b),
    "down": lambda a, b: (a + 1, b),
    "left": lambda a, b: (a, b - 1),
    "right": lambda a, b: (a, b + 1)
}

for direction in directions:
    next_row, next_col = up_down_left_right[direction](miner_row, miner_col)
    if next_row >= size or next_col >= size or next_row < 0 or next_col < 0:
        continue
    miner_row, miner_col = next_row, next_col
    if matrix[miner_row][miner_col] == "c":
        matrix[miner_row][miner_col] = "*"
        c_collected += 1
        if c_collected == c_count:
            print(f"You collected all coal! ({miner_row}, {miner_col})")
            sys.exit()
    elif matrix[miner_row][miner_col] == "e":
        print(f"Game over! ({miner_row}, {miner_col})")
        sys.exit()

print(f"{c_count - c_collected} pieces of coal left. ({miner_row}, {miner_col})")

# ------------------------------------------------------------------------------------------


