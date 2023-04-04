import math
days = int(input())
food_kg = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

eaten_food = (dog_food + cat_food + turtle_food/1000)*days

if food_kg >= eaten_food:
    print(f"{math.floor(food_kg-eaten_food)} kilos of food left.")
else:
    print(f"{math.ceil(eaten_food-food_kg)} more kilos of food are needed.")