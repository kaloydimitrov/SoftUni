rows, cols = [int(x) for x in input().split(", ")]

matrix = []

y_row = 0
y_col = 0

count_of_all_elements = 0

for r in range(rows):
    line = list(input().replace(" ", ""))
    matrix.append(line)

    for c in range(cols):
        if line[c] == "Y":
            y_row, y_col = r, c
            matrix[y_row][y_col] = "x"
        if line[c] == "D" or line[c] == "G" or line[c] == "C":
            count_of_all_elements += 1

up_down_left_right = {
    "up": lambda a, b: (a - 1, b),
    "down": lambda a, b: (a + 1, b),
    "left": lambda a, b: (a, b - 1),
    "right": lambda a, b: (a, b + 1)
}

command = input()

count_of_all_elements_in_while = 0
count_of_ds = 0
count_of_gs = 0
count_of_cs = 0

do_break = False

while command != "End":
    move_command = command.split("-")
    direction, steps = move_command[0], int(move_command[1])

    for _ in range(steps):
        y_row, y_col = up_down_left_right[direction](y_row, y_col)
        if 0 > y_row or 0 > y_col or rows <= y_row or cols <= y_col:
            if direction == "up":
                y_row = rows - 1
            if direction == "down":
                y_row = 0
            if direction == "left":
                y_col = cols - 1
            if direction == "right":
                y_col = 0

        if matrix[y_row][y_col] == "D":
            count_of_all_elements_in_while += 1
            count_of_ds += 1
        if matrix[y_row][y_col] == "G":
            count_of_all_elements_in_while += 1
            count_of_gs += 1
        if matrix[y_row][y_col] == "C":
            count_of_all_elements_in_while += 1
            count_of_cs += 1

        matrix[y_row][y_col] = "x"

        if count_of_all_elements == count_of_all_elements_in_while:
            do_break = True
            break

    if do_break:
        break

    command = input()

matrix[y_row][y_col] = "Y"

if do_break:
    print("Merry Christmas!")

print("You've collected:")

print(f"- {count_of_ds} Christmas decorations")
print(f"- {count_of_gs} Gifts")
print(f"- {count_of_cs} Cookies")

for r in matrix:
    print(" ".join(r))
