string = list(input())

while string:
    print(string.pop(), end="")

# --------------------------------------------------------------------------------------------

expression = input()

stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)
    elif expression[index] == ")":
        print(expression[stack.pop():index + 1])

# --------------------------------------------------------------------------------------------

from collections import deque

people = deque()

while True:
    command = input()
    if command == "End":
        print(f"{len(people)} people remaining.")
        break
    elif command == "Paid":
        while people:
            print(people.popleft())
    else:
        people.append(command)


# --------------------------------------------------------------------------------------------

from collections import deque

queue = deque()
water = int(input())

command = input()

while command != "Start":
    queue.append(command)
    command = input()

second_command = input()

while second_command != "End":
    if "refill" in second_command:
        data = int(second_command.split()[1])
        water += data
    else:
        int_water = int(second_command)
        if int_water <= water:
            water -= int_water
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")

    second_command = input()

print(f"{water} liters left")

# --------------------------------------------------------------------------------------------

from collections import deque

people = deque(input().split())
toss = int(input())

counter = 1

while people:
    if len(people) == 1:
        print(f"Last is {people.popleft()}")
    elif counter == toss:
        print(f"Removed {people.popleft()}")
        counter = 0
    else:
        current = people.popleft()
        people.append(current)

    counter += 1
