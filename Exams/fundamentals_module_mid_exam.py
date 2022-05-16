# --------------------------------------------------------------------------------------------   01. Swimming Championship

days_of_the_championship = int(input())
points_that_need_to_be_covered = int(input())
count_of_the_swimmers = int(input())
hotel_room_price_for_a_day_for_one_swimmer = float(input())
participation_fee_per_swimmer = float(input())

hotel_price = hotel_room_price_for_a_day_for_one_swimmer * count_of_the_swimmers * days_of_the_championship
participation_price = participation_fee_per_swimmer * count_of_the_swimmers

money_left_to_pay = hotel_price + participation_price

points = 0
successful = False

for day in range(1, days_of_the_championship + 1):
    if day != 1:
        points += current_points * 0.05

    current_points = float(input())
    points += current_points

    if points >= points_that_need_to_be_covered:
        successful = True
        break

if successful:
    money_left_to_pay *= 0.75
    print(f"Money left to pay: {money_left_to_pay:.2f} BGN.")
    print("The championship was successful!")
else:
    money_left_to_pay *= 0.90
    print(f"Money left to pay: {money_left_to_pay:.2f} BGN.")
    print("The championship was not successful.")

# --------------------------------------------------------------------------------------------   02. Generating Numbers

numbers = list(map(int, input().split()))

command = input()

while command != "END":
    if "add to start" in command:
        data = command.split("add to start")
        nums = data[1].split()
        nums = [int(x) for x in nums]
        for num in range(len(nums)):
            numbers.insert(num, nums[num])

    elif "remove greater than" in command:
        data1 = command.split("remove greater than")
        value = int(data1[1])

        numbers = [x for x in numbers if x <= value]

    elif "replace" in command:
        data2 = command.split()
        value1 = int(data2[1])
        replacement = int(data2[2])

        for it in range(len(numbers)):
            if numbers[it] == value1:
                numbers[it] = replacement
                break

    elif "remove at index" in command:
        data3 = command.split("remove at index")
        index = int(data3[1])

        if 0 <= index < len(numbers):
            numbers.remove(numbers[index])

    elif "find even" in command:
        evens = []
        for el in numbers:
            if el % 2 == 0:
                evens.append(str(el))

        print(" ".join(evens))
    elif "find odd" in command:
        odds = []
        for el1 in numbers:
            if el1 % 2 != 0:
                odds.append(str(el1))

        print(" ".join(odds))

    command = input()


numbers = [str(x) for x in numbers]
print(", ".join(numbers))

# --------------------------------------------------------------------------------------------   03. Grocery Shopping

products = input().split("|")

command = input()

while command != "Shop!":
    data = command.split("%")
    action = data[0]

    if action == "Important":
        product1 = data[1]

        if product1 in products:
            products.remove(product1)
            products.insert(0, product1)
        else:
            products.insert(0, product1)

    elif action == "Add":
        product2 = data[1]

        last_index = products.index(products[-1]) + 1
        if product2 not in products:
            products.insert(last_index, product2)
        else:
            print("The product is already in the list.")

    elif action == "Swap":
        first_product = data[1]
        second_product = data[2]

        if first_product not in products:
            print(f"Product {first_product} missing!")
        elif second_product not in products:
            print(f"Product {second_product} missing!")
        else:
            first_product_index = products.index(first_product)
            second_product_index = products.index(second_product)

            products[first_product_index], products[second_product_index] = products[second_product_index], products[first_product_index]

    elif action == "Remove":
        product3 = data[1]

        if product3 in products:
            products.remove(product3)
        else:
            print(f"Product {product3} isn't in the list.")

    elif action == "Reversed":
        products.reverse()

    command = input()

for number in range(len(products)):
    print(f"{number+1}. {products[number]}")
