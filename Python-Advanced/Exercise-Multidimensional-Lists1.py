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

pass

# ------------------------------------------------------------------------------------------

r, c = [int(x) for x in input().split(" ")]

matrix = []

for _ in range(r):
    matrix.append([int(x) for x in input().split(" ")])

biggest_square = 0
biggest_row = 0
biggest_col = 0

for row in range(r - 2):
    for col in range(c - 2):
        square = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if square > biggest_square:
            biggest_square = square
            biggest_row = row
            biggest_col = col

print(f"Sum = {biggest_square}")
print(f"{matrix[biggest_row][biggest_col]} {matrix[biggest_row][biggest_col + 1]} {matrix[biggest_row][biggest_col + 2]}")
print(f"{matrix[biggest_row + 1][biggest_col]} {matrix[biggest_row + 1][biggest_col + 1]} {matrix[biggest_row + 1][biggest_col + 2]}")
print(f"{matrix[biggest_row + 2][biggest_col]} {matrix[biggest_row + 2][biggest_col + 1]} {matrix[biggest_row + 2][biggest_col + 2]}")

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
