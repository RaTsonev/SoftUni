import math
days = int(input())
food_kg = int(input())
food_day_dog_kg = float(input())
food_day_cat_kg = float(input())
food_day_turtle_kg = float(input())

dog_food = days*food_day_dog_kg
cat_food = days*food_day_cat_kg
turtle_food = days*food_day_turtle_kg/1000
food_needed = dog_food + cat_food + turtle_food

if food_kg >= food_needed:
    diff = math.floor(abs(food_kg - food_needed))
    print(f"{diff} kilos of food left.")
else:
    diff = math.ceil(abs(food_kg - food_needed))
    print(f"{diff} more kilos of food are needed.")