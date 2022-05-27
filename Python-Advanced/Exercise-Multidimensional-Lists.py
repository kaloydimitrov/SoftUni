number = int(input())

matrix = []

for _ in range(number):
    current_raw = [int(x) for x in input().split()]
    matrix.append(current_raw)

command = input()

while command != "END":
    current_command = command.split()
    action, row, col, value = current_command[0], int(current_command[1]), int(current_command[2]), int(current_command[3])

    if row < 0 or col < 0 or row >= number or col >= number:
        print("Invalid coordinates")
    else:
        if action == "Add":
            matrix[row][col] += value
        elif action == "Subtract":
            matrix[row][col] -= value

    command = input()

for i in range(len(matrix)):
    current_row = [str(x) for x in matrix[i]]
    print(" ".join(current_row))
