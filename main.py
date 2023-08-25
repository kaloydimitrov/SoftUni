cubic_meters = int(input()) * int(input()) * int(input())
value = 0
no_more_space = False

command = input()

while command != 'Done':
    value += int(command)

    if value > cubic_meters:
        no_more_space = True
        break

    command = input()

if no_more_space:
    print(f"No more free space! You need {value - cubic_meters} Cubic meters more.")
else:
    print(f"{cubic_meters - value} Cubic meters left.")
