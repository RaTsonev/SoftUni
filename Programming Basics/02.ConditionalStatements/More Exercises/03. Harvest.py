import math
area_meters = int(input())
grapes_per_meter = float(input())
wine_needed = int(input())
workers = int(input())

whole_grapes = area_meters*grapes_per_meter
wine_production = whole_grapes*0.4/2.5

if wine_needed > wine_production:
    diff = math.floor(wine_needed-wine_production)
    print(f"It will be a tough winter! More {diff:.0f} liters wine needed.")
else:
    wine_production = math.floor(wine_production)
    print(f"Good harvest this year! Total wine: {wine_production} liters.")
    diff = math.ceil(wine_production-wine_needed)
    wine_per_worker = math.ceil(diff/workers)
    print(f"{diff:} liters left -> {wine_per_worker} liters per person.")
