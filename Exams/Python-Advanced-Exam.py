# --------------------------------------------------------------------------------------------   01. Collecting Eggs

from collections import deque

eggs = deque(int(x) for x in input().split(", "))
papers = [int(x) for x in input().split(", ")]

boxes = 0

while True:
    if not eggs or not papers:
        break

    current_egg = eggs.popleft()

    if current_egg <= 0:
        continue
    if current_egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    current_paper = papers.pop()

    if current_egg + current_paper <= 50:
        boxes += 1

if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if papers:
    print(f"Pieces of paper left: {', '.join([str(x) for x in papers])}")

# --------------------------------------------------------------------------------------------   02. Exit Founder

players = input().split(", ")
first_player = players[0]
second_player = players[1]

matrix = []

for _ in range(6):
    line = input().replace(" ", "")
    matrix.append(list(line))


def find_row_col(text):
    current_command = text.replace("(", "")
    final_command = current_command.replace(")", "")
    row, col = [int(x) for x in final_command.split(", ")]
    return row, col


tom_banned = False
tom_counter = 0
jerry_banned = False
jerry_counter = 0

while True:
    current_player = players[0]
    other_player = players[1]
    current_row, current_col = find_row_col(input())

    if current_player == "Tom" and tom_banned:
        tom_counter += 1
        if tom_counter == 2:
            tom_banned = False
            tom_counter = 0
        else:
            players = players[::-1]
            continue

    if current_player == "Jerry" and jerry_banned:
        jerry_counter += 1
        if jerry_counter == 2:
            jerry_banned = False
            jerry_counter = 0
        else:
            players = players[::-1]
            continue

    if matrix[current_row][current_col] == "W":
        if current_player == "Tom":
            tom_banned = True
        if current_player == "Jerry":
            jerry_banned = True

        print(f"{current_player} hits a wall and needs to rest.")

    if matrix[current_row][current_col] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    if matrix[current_row][current_col] == "T":
        print(f"{current_player} is out of the game! The winner is {other_player}.")
        break

    players = players[::-1]


# --------------------------------------------------------------------------------------------   03. Shopping Cart

def any_items(pm):
    elements = False
    for l in pm.values():
        if len(l) > 0:
            elements = True
    if elements:
        return True
    else:
        return False


def shopping_cart(*args):
    soup_counter = 0
    pizza_counter = 0
    dessert_counter = 0

    product_meals = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []
    }

    for t in args:
        if t == "Stop":
            break

        product, meal = t

        if product == "Soup":
            if soup_counter == 3:
                continue
        if product == "Dessert":
            if dessert_counter == 2:
                continue
        if product == "Pizza":
            if pizza_counter == 4:
                continue

        if meal in product_meals[product]:
            continue
        product_meals[product].append(meal)

        if product == "Soup":
            soup_counter += 1
        if product == "Dessert":
            dessert_counter += 1
        if product == "Pizza":
            pizza_counter += 1

    result = ""

    if not any_items(product_meals):
        result = "No products in the cart!"
    else:
        sort = sorted(product_meals.items(), key=lambda x: (-len(x[1]), x[0]))
        for key, value in sort:
            sorted_value = sorted(value)
            result += f"{key}:" + "\n"
            for sv in sorted_value:
                result += f" - {sv}" + "\n"

    return result
