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


