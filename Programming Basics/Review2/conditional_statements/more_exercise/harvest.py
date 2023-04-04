import math
vineyard_meters = int(input())
grapes_per_meter = float(input())
wine_needed = int(input())
workers = int(input())

grapes_for_wine = vineyard_meters * grapes_per_meter*0.4
wine_liters = grapes_for_wine/2.5
wine_left = wine_liters-wine_needed
if wine_needed > wine_liters:
    print(f"It will be a tough winter! More {math.floor(wine_needed-wine_liters)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(wine_liters)} liters.")
    print(f"{math.ceil(wine_left)} liters left -> {math.ceil(wine_left/workers)} liters per person.")