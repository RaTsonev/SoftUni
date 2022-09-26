import math

vineyard_sm = int(input())
grapes_for_one_sm = float(input())
needed_wine = int(input())
workers = int(input())

grapes = vineyard_sm*grapes_for_one_sm
liters_wine = (grapes*0.4)/2.5
if liters_wine < needed_wine:
    diff = math.floor(needed_wine - liters_wine)
    print(f"It will be a tough winter! More {diff:.0f} liters wine needed.")
if liters_wine >= needed_wine:
    print(f"Good harvest this year! Total wine: {math.floor(liters_wine)} liters.")
    diff = abs(math.ceil(needed_wine - liters_wine))
    wine_per_worker = math.ceil(diff/workers)
    print(f"{diff} liters left -> {wine_per_worker} liters per person.")