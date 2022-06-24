from collections import deque

bomb_effects = deque(int(x) for x in input().split(", "))
bomb_casings = [int(x) for x in input().split(", ")]

d = {
    60: 0,
    40: 0,
    120: 0
}

success = False

while True:
    bomb_effect = bomb_effects.popleft()
    bomb_casing = bomb_casings.pop()

    if bomb_effect + bomb_casing in d.keys():
        d[bomb_effect + bomb_casing] += 1
    else:
        bomb_effects.appendleft(bomb_effect)
        bomb_casing -= 5
        bomb_casings.append(bomb_casing)

    ready_bomb_types = 0
    for value in d.values():
        if value >= 3:
            ready_bomb_types += 1
    if ready_bomb_types == 3:
        success = True

    if not bomb_effects or not bomb_casings or success:
        break


if success:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")

bombs = [x for x in d.values()]
print(f"Cherry Bombs: {bombs[0]}")
print(f"Datura Bombs: {bombs[1]}")
print(f"Smoke Decoy Bombs: {bombs[2]}")
