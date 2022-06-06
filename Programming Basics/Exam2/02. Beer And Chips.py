import math
name_fan = input()
budget = float(input())
beer_counter = int(input())
chips_counter = int(input())

beer = beer_counter * 1.2
chips = math.ceil(chips_counter * beer*45/100)
sum = beer + chips
diff = abs(budget-sum)
if budget >= sum:
    print(f"{name_fan} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{name_fan} needs {diff:.2f} more leva!")