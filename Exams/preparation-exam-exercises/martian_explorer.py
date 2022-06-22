matrix = []

e_row = 0
e_col = 0

for r in range(6):
    line = input().split()
    matrix.append(line)
    for c in range(6):
        if line[c] == "E":
            e_row = r
            e_col = c

up_down_left_right = {
    "up": lambda a, b: (a - 1, b),
    "down": lambda a, b: (a + 1, b),
    "left": lambda a, b: (a, b - 1),
    "right": lambda a, b: (a, b + 1)
}

w_found = False
c_found = False
m_found = False

for direction in input().split(", "):
    next_row, next_col = up_down_left_right[direction](e_row, e_col)
    if next_row < 0 or next_col < 0 or next_row >= 6 or next_col >= 6:
        if direction == "up":
            next_row = 5
        elif direction == "down":
            next_row = 0
        elif direction == "left":
            next_col = 5
        elif direction == "right":
            next_col = 0

    e_row, e_col = next_row, next_col

    if matrix[e_row][e_col] == "W":
        print(f"Water deposit found at ({e_row}, {e_col})")
        w_found = True
    elif matrix[e_row][e_col] == "C":
        print(f"Concrete deposit found at ({e_row}, {e_col})")
        c_found = True
    elif matrix[e_row][e_col] == "M":
        print(f"Metal deposit found at ({e_row}, {e_col})")
        m_found = True
    elif matrix[e_row][e_col] == "R":
        print(f"Rover got broken at ({e_row}, {e_col})")
        break

if w_found and c_found and m_found:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
