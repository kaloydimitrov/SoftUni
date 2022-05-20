string = list(input())
answer = ''

while string:
    char = string.pop()
    answer += char

print(answer)

# --------------------------------------------------------------------------------------------

expression = input()
stack = []

for index in range(len(expression)):
    if expression[index] == '(':
        stack.append(index)
    elif expression[index] == ')':
        bracket = stack.pop()
        print(expression[bracket:index + 1])

# --------------------------------------------------------------------------------------------

from collections import deque

q = deque()

while True:
    command = input()
    if command == 'Paid':
        while q:
            print(q.popleft())
    elif command == 'End':
        print(f"{len(q)} people remaining.")
        break
    else:
        q.append(command)

# --------------------------------------------------------------------------------------------

from collections import deque

water = int(input())
people = deque()

command = input()

while command != "Start":
    people.append(command)
    command = input()

second_command = input()

while second_command != "End":
    if "refill" in second_command:
        water += int(second_command.split()[1])
    else:
        person = people.popleft()
        if int(second_command) > water:
            print(f"{person} must wait")
        else:
            print(f"{person} got water")
            water -= int(second_command)

    second_command = input()

print(str(water) + " liters left")

# --------------------------------------------------------------------------------------------

from collections import deque

kids = deque(input().split())

toss = int(input())
counter = 0

while len(kids) > 1:
    kid = kids.popleft()
    counter += 1

    if counter == toss:
        counter = 0
        print(f"Removed {kid}")
    else:
        kids.append(kid)

print("Last is " + kids[0])
