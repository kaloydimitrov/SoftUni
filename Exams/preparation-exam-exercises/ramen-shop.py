from collections import deque

bowls_of_ramen = [int(x) for x in input().split(", ")]
customers = deque(int(x) for x in input().split(", "))

while True:
    bowl = bowls_of_ramen.pop()
    customer = customers.popleft()
    if bowl > customer:
        bowl -= customer
        bowls_of_ramen.append(bowl)
    elif customer > bowl:
        customer -= bowl
        customers.appendleft(customer)

    if not customers:
        print("Great job! You served all the customers.")
        break
    if not bowls_of_ramen:
        print("Out of ramen! You didn't manage to serve all customers.")
        break

if bowls_of_ramen:
    print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls_of_ramen])}")
if customers:
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
