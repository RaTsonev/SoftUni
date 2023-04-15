budget = float(input())
extra = int(input())
clothes_per_extra = float(input())

decor = budget * 0.1
sum_clothes = extra * clothes_per_extra
if extra >= 150:
    sum_clothes -= sum_clothes * 0.1

cost = decor + sum_clothes

if budget >= cost:
    print("Action!")
    print(f"Wingard starts filming with {budget-cost:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {cost - budget:.2f} leva more.")