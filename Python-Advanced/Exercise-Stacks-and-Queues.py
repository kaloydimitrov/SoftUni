nums = input().split()

while nums:
    print(nums.pop(), end=' ')

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

from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))


while True:
    if food < orders[0]:
        print(f"Orders left: {' '.join([str(d) for d in orders])}")
        break
    else:
        food -= orders.popleft()
    if len(orders) == 0:
        print(f"Orders complete")
        break

# --------------------------------------------------------------------------------------------

clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

current_rack_capacity = rack_capacity
rack_counter = 1

while clothes:
    piece_of_clothing = clothes[-1]
    if piece_of_clothing > current_rack_capacity:
        rack_counter += 1
        current_rack_capacity = rack_capacity
    else:
        current_rack_capacity -= piece_of_clothing
        clothes.pop()

print(rack_counter)

# --------------------------------------------------------------------------------------------


