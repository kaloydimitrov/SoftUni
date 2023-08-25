days = int(input()) - 1
room_type = input()
review = input()

final_price = 0


def apply_discount():
    global final_price

    if room_type == 'apartment':
        if days < 10:
            final_price *= 0.70
        elif 10 < days < 15:
            final_price *= 0.65
        elif days > 15:
            final_price *= 0.50
    elif room_type == 'president apartment':
        if days < 10:
            final_price *= 0.90
        elif 10 < days < 15:
            final_price *= 0.85
        elif days > 15:
            final_price *= 0.80


if room_type == 'room for one person':
    final_price += 18 * days
    apply_discount()
elif room_type == 'apartment':
    final_price += 25 * days
    apply_discount()
elif room_type == 'president apartment':
    final_price += 35 * days
    apply_discount()


if review == 'positive':
    final_price *= 1.25
elif review == 'negative':
    final_price *= 0.90

print(f"{final_price:.2f}")
