matrix = []
k_row = 0
k_col = 0

for r in range(8):
    line = input().split()
    matrix.append(line)
    for c in range(8):
        if line[c] == "K":
            k_row = r
            k_col = c

directions = {
    "up": lambda a, b: (a - 1, b),
    "down": lambda a, b: (a + 1, b),
    "left": lambda a, b: (a, b - 1),
    "right": lambda a, b: (a, b + 1),
    "up_right": lambda a, b: (a - 1, b + 1),
    "down_left": lambda a, b: (a + 1, b - 1),
    "up_left": lambda a, b: (a - 1, b - 1),
    "down_right": lambda a, b: (a + 1, b + 1)
}

king_captures = []

for row in range(8):
    for col in range(8):
        if matrix[row][col] == "Q":
            for direction in directions:
                current_row = row
                current_col = col
                while True:
                    next_row, next_col = directions[direction](current_row, current_col)
                    if next_row < 0 or next_col < 0 or next_row >= 8 or next_col >= 8 or matrix[next_row][next_col] == "Q":
                        break
                    current_row, current_col = next_row, next_col

                    if matrix[current_row][current_col] == "K":
                        king_captures.append([row, col])

if king_captures:
    [print(x) for x in king_captures]
else:
    print("The king is safe!")
