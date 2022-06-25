# --------------------------------------------------------------------------------------------   01. Moon

import math

speed = float(input())
needed_liters_of_fuel = float(input())

round_trip = 384400 * 2
round_trip_time = round_trip / speed

total_time = math.ceil(round_trip_time) + 3
fuel = (needed_liters_of_fuel * round_trip) / 100

print(total_time)
print(int(fuel))

# --------------------------------------------------------------------------------------------   02. Beer And Chips

import math

name = input()
budget = float(input())
beer = int(input()) * 1.20
chips = int(input())

percent = (beer * 45) / 100
total_chips = percent * chips
total_sum = beer + math.ceil(total_chips)

if total_sum <= budget:
    dis = budget - total_sum
    print(f"{name} bought a snack and has {dis:.2f} leva left.")
else:
    dis = total_sum - budget
    print(f"{name} needs {dis:.2f} more leva!")

# --------------------------------------------------------------------------------------------   03. Computer Room

month = input()
hours = int(input())
people_in_group = int(input())
day_or_night = input()
sum_per_hour = 0

if month == 'march' or month == 'april' or month == 'may':
    if day_or_night == 'day':
        sum_per_hour = 10.50
    else:
        sum_per_hour = 8.40
elif month == 'june' or month == 'july' or month == 'august':
    if day_or_night == 'day':
        sum_per_hour = 12.60
    else:
        sum_per_hour = 10.20

if people_in_group >= 4:
    sum_per_hour *= 0.90
if hours >= 5:
    sum_per_hour *= 0.50

print(f"Price per person for one hour: {sum_per_hour:.2f}")
total_price = (sum_per_hour * people_in_group) * hours
print(f"Total cost of the visit: {total_price:.2f}")

# --------------------------------------------------------------------------------------------   04. Cat Food

cats = int(input())
total_food = 0
cats_in_group1 = 0
cats_in_group2 = 0
cats_in_group3 = 0

for r in range(cats):
    food = float(input())
    total_food += food
    if 100 <= food < 200:
        cats_in_group1 += 1
    elif 200 <= food < 300:
        cats_in_group2 += 1
    elif 300 <= food < 400:
        cats_in_group3 += 1

needed_calculation = total_food / 1000
price_for_food_per_day = needed_calculation * 12.45

print(f"Group 1: {cats_in_group1} cats.")
print(f"Group 2: {cats_in_group2} cats.")
print(f"Group 3: {cats_in_group3} cats.")
print(f"Price for food per day: {price_for_food_per_day:.2f} lv.")

# --------------------------------------------------------------------------------------------   05. Puppy Care

purchased_food_for_puppy = int(input()) * 1000
total_food_puppy_ate = 0
command = input()

while command != 'Adopted':
    total_food_puppy_ate += int(command)
    command = input()

if purchased_food_for_puppy >= total_food_puppy_ate:
    dis = purchased_food_for_puppy - total_food_puppy_ate
    print(f"Food is enough! Leftovers: {dis} grams.")
else:
    dis = total_food_puppy_ate - purchased_food_for_puppy
    print(f"Food is not enough. You need {dis} grams more.")

# --------------------------------------------------------------------------------------------   06. Gold Mine

number_of_locations = int(input())
average_yield = 0

for loc in range(number_of_locations):
    sum_of_all_gold_in_all_days = 0
    intended_gold_per_day = float(input())
    days_in_one_location = int(input())
    for days in range(days_in_one_location):
        gold_per_day = float(input())
        sum_of_all_gold_in_all_days += gold_per_day
        average_yield = sum_of_all_gold_in_all_days / days_in_one_location
    if average_yield >= intended_gold_per_day:
        print(f"Good job! Average gold per day: {average_yield:.2f}.")
    elif intended_gold_per_day > average_yield:
        dis = intended_gold_per_day - average_yield
        print(f'You need {dis:.2f} gold.')
