import math
days_number = int(input())
food_kg = int(input())
food_dog_per_day = float(input())
food_cat_per_day = float(input())
food_turtle_per_day = float(input())/1000

eaten_food = days_number * (food_dog_per_day + food_cat_per_day + food_turtle_per_day)
if food_kg >= eaten_food:
    diff = math.floor(abs(eaten_food - food_kg))
    print(f"{diff} kilos of food left.")
else:
    diff = math.ceil(abs(eaten_food - food_kg))
    print(f"{diff} more kilos of food are needed.")