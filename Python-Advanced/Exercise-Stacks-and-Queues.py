

# --------------------------------------------------------------------------------------------

iter_times = int(input())
stack = []

for _ in range(iter_times):
    querie = input().split()

    if querie[0] == "1":
        stack.append(querie[1])
    elif querie[0] == "2" and stack:
        stack.pop()
    elif querie[0] == "3" and stack:
        print(max(stack))
    elif querie[0] == "4" and stack:
        print(min(stack))

stack = stack[::-1]

print(", ".join(stack))

# --------------------------------------------------------------------------------------------

