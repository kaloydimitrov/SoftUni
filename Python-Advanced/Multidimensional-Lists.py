rows, elements_in_row = [int(x) for x in input().split(", ")]
total_sum = 0
matrix = []

for row in range(rows):
    current_input = [int(x) for x in input().split(", ")]
    total_sum += sum(current_input)
    matrix.append(current_input)

print(total_sum)
print(matrix)

# ---------------------------------------------------------------------------

matrix = []

for index in range(int(input())):
    current_line = [int(x) for x in input().split(", ")]
    matrix.append([])
    for num in current_line:
        if num % 2 == 0:
            matrix[index].append(num)

print(matrix)

# ---------------------------------------------------------------------------

matrix = []

for _ in range(int(input())):
    line = [int(x) for x in input().split(", ")]
    [matrix.append(x) for x in line]

print(matrix)

# ---------------------------------------------------------------------------

rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for c in range(cols):
    current_sum = 0
    for r in range(rows):
        a = matrix[r][c]
        current_sum += a

    print(current_sum)

# ---------------------------------------------------------------------------

num = int(input())
matrix = []

for _ in range(num):
    matrix.append([int(x) for x in input().split()])

counter = 0
total_sum = 0

for row in matrix:
    a = row[counter]
    total_sum += a
    counter += 1

# ---------------------------------------------------------------------------

row_n_col = int(input())

matrix = []

result = None

for r in range(row_n_col):
    chars = list(input())
    matrix.append(chars)

searched_element = input()

for row in range(row_n_col):
    if result is not None:
        break
    for col in range(row_n_col):
        if matrix[row][col] == searched_element:
            result = f"({row}, {col})"
            break

if result is None:
    print(f"{searched_element} does not occur in the matrix")
else:
    print(result)

# ---------------------------------------------------------------------------

rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for r in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)


biggest_sum = 0
biggest_row_col = ()

for row in range(rows - 1):
    for col in range(cols - 1):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            biggest_row_col = (row, col)

print(f"{matrix[biggest_row_col[0]][biggest_row_col[1]]} {matrix[biggest_row_col[0]][biggest_row_col[1] + 1]}")
print(f"{matrix[biggest_row_col[0] + 1][biggest_row_col[1]]} {matrix[biggest_row_col[0] + 1][biggest_row_col[1] + 1]}")

print(biggest_sum)
