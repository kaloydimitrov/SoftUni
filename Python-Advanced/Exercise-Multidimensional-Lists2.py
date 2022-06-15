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

biggest_key = ""
biggest_value = -math.inf
biggest_steps = []

for action in up_down_left_right:
    row = bunny_row
    col = bunny_col

    current_sum = 0
    current_steps = []

    row, col = up_down_left_right[action](row, col)

    while 0 <= row < size and 0 <= col < size and matrix[row][col] != "X":
        current_sum += int(matrix[row][col])
        current_steps.append(f"[{row}, {col}]")

        row, col = up_down_left_right[action](row, col)

    if current_sum > biggest_value and current_steps:
        biggest_key = action
        biggest_value = current_sum
        biggest_steps = current_steps

print(biggest_key)
[print(x) for x in biggest_steps]
print(biggest_value)

# --------------------------------------------------

size = int(input())

matrix = []

alice_row = 0
alice_col = 0

for r in range(size):
    current_col = input().split(" ")
    matrix.append(current_col)

    for c in range(size):
        if current_col[c] == "A":
            matrix[r][c] = "*"
            alice_row = r
            alice_col = c

up_down_left_right = {
    "up": lambda a, b: (a - 1, b),
    "down": lambda a, b: (a + 1, b),
    "left": lambda a, b: (a, b - 1),
    "right": lambda a, b: (a, b + 1)
}

bags_of_tea = 0
alice_made_it = True

while True:
    current_command = input()

    alice_row, alice_col = up_down_left_right[current_command](alice_row, alice_col)
    if alice_row < 0 or alice_col < 0 or alice_row >= size or alice_col >= size:
        alice_made_it = False
        break

    current_symbol = matrix[alice_row][alice_col]
    matrix[alice_row][alice_col] = "*"

    if current_symbol == "R":
        alice_made_it = False
        break

    if current_symbol.isnumeric():
        bags_of_tea += int(current_symbol)
        if bags_of_tea >= 10:
            break

if alice_made_it:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for print_row in matrix:
    print(" ".join(print_row))

# --------------------------------------------------

matrix = []

my_row = 0
my_col = 0

start_x_count = 0

for r in range(5):
    current_col = input().split(" ")
    matrix.append(current_col)
    for c in range(5):
        if current_col[c] == "A":
            my_row = r
            my_col = c
        elif current_col[c] == "x":
            start_x_count += 1

up_down_left_right = {
    "up": lambda a, b: (a - 1, b),
    "down": lambda a, b: (a + 1, b),
    "left": lambda a, b: (a, b - 1),
    "right": lambda a, b: (a, b + 1)
}

shot_targets = []
mid_x_count = 0

for _ in range(int(input())):
    command = input().split()
    action = command[0]
    turn = command[1]

    if action == "shoot":
        shoot_row, shoot_col = my_row, my_col
        while True:
            shoot_row, shoot_col = up_down_left_right[turn](shoot_row, shoot_col)
            if shoot_row < 0 or shoot_col < 0 or shoot_row >= 5 or shoot_col >= 5:
                break
            if matrix[shoot_row][shoot_col] == "x":
                shot_targets.append(f"[{shoot_row}, {shoot_col}]")
                matrix[shoot_row][shoot_col] = "."
                break

    elif action == "move":
        steps = int(command[2])
        next_row, next_col = my_row, my_col

        if turn == "up":
            next_row -= steps
        if turn == "down":
            next_row += steps
        if turn == "left":
            next_col -= steps
        if turn == "right":
            next_col += steps

        if next_row < 0 or next_col < 0 or next_row >= 5 or next_col >= 5 or matrix[next_row][next_col] != ".":
            continue

        my_row, my_col = next_row, next_col

    for row in range(5):
        for col in range(5):
            if matrix[row][col] == "x":
                mid_x_count += 1

    if mid_x_count == 0:
        break

    mid_x_count = 0

end_x_count = 0

for row in range(5):
    for col in range(5):
        if matrix[row][col] == "x":
            end_x_count += 1

if end_x_count == 0:
    print(f"Training completed! All {start_x_count} targets hit.")
else:
    print(f"Training not completed! {end_x_count} targets left.")

[print(x) for x in shot_targets]

# --------------------------------------------------

presents = int(input())
size = int(input())

santa_row = 0
santa_col = 0

matrix = []

nice_kids = 0

for r in range(size):
    line = input().split()
    matrix.append(line)

    for c in range(size):
        if line[c] == "S":
            santa_row = r
            santa_col = c
        elif line[c] == "V":
            nice_kids += 1

matrix[santa_row][santa_col] = "-"

up_down_left_right = {
    "up": lambda a, b: (a - 1, b),
    "down": lambda a, b: (a + 1, b),
    "left": lambda a, b: (a, b - 1),
    "right": lambda a, b: (a, b + 1)
}


def count_nice_kids():
    n_kids = 0
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "V":
                n_kids += 1

    return n_kids


while True:
    direction = input()
    if direction == "Christmas morning":
        break

    santa_row, santa_col = up_down_left_right[direction](santa_row, santa_col)

    if matrix[santa_row][santa_col] == "V":
        presents -= 1

    elif matrix[santa_row][santa_col] == "C":
        if matrix[santa_row - 1][santa_col] in "VX":
            matrix[santa_row - 1][santa_col] = "-"
            presents -= 1
        if matrix[santa_row + 1][santa_col] in "VX":
            matrix[santa_row + 1][santa_col] = "-"
            presents -= 1
        if matrix[santa_row][santa_col - 1] in "VX":
            matrix[santa_row][santa_col - 1] = "-"
            presents -= 1
        if matrix[santa_row][santa_col + 1] in "VX":
            matrix[santa_row][santa_col + 1] = "-"
            presents -= 1

    matrix[santa_row][santa_col] = "-"

    if presents <= 0 and count_nice_kids() > 0:
        print("Santa ran out of presents!")
        break
    if presents <= 0:
        break

matrix[santa_row][santa_col] = "S"
[print(" ".join(x)) for x in matrix]

if count_nice_kids() <= 0:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {count_nice_kids()} nice kid/s.")
