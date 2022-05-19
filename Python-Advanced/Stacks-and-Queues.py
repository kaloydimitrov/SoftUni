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

