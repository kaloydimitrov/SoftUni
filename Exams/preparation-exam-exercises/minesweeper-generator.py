matrix = []

iteration = int(input())

for ri in range(iteration):
    matrix.append([])
    for _ in range(iteration):
        matrix[ri].append(0)

for _ in range(int(input())):
    coordinates = input()
    coordinates = coordinates.replace("(", "")
    coordinates = coordinates.replace(")", "")
    row, col = [int(x) for x in coordinates.split(", ")]

    matrix[row][col] = "*"


def is_valid(r, c):
    if 0 <= r < iteration and 0 <= c < iteration:
        return True
    else:
        return False


for row in range(iteration):
    for col in range(iteration):
        if matrix[row][col] != "*":

            if is_valid(row - 1, col) and matrix[row - 1][col] == "*":
                matrix[row][col] += 1
            if is_valid(row + 1, col) and matrix[row + 1][col] == "*":
                matrix[row][col] += 1
            if is_valid(row, col - 1) and matrix[row][col - 1] == "*":
                matrix[row][col] += 1
            if is_valid(row, col + 1) and matrix[row][col + 1] == "*":
                matrix[row][col] += 1

            if is_valid(row - 1, col - 1) and matrix[row - 1][col - 1] == "*":
                matrix[row][col] += 1
            if is_valid(row - 1, col + 1) and matrix[row - 1][col + 1] == "*":
                matrix[row][col] += 1
            if is_valid(row + 1, col - 1) and matrix[row + 1][col - 1] == "*":
                matrix[row][col] += 1
            if is_valid(row + 1, col + 1) and matrix[row + 1][col + 1] == "*":
                matrix[row][col] += 1

for row in matrix:
    print(*row, sep=" ")
