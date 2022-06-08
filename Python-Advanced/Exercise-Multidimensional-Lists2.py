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

pass
