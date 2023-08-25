month = input()
nights = int(input())

final_ap_price, final_st_price = 0, 0

if month == 'May' or month == 'October':
    final_ap_price, final_st_price = nights * 65, nights * 50

    if nights > 14:
        final_st_price *= 0.70
    elif nights > 7:
        final_st_price *= 0.95
elif month == 'June' or month == 'September':
    final_ap_price, final_st_price = nights * 68.70, nights * 75.20

    if nights > 14:
        final_st_price *= 0.80
elif month == 'July' or month == 'August':
    final_ap_price, final_st_price = nights * 77, nights * 76

if nights > 14:
    final_ap_price *= 0.90

print(f"Apartment: {final_ap_price:.2f} lv.")
print(f"Studio: {final_st_price:.2f} lv.")
