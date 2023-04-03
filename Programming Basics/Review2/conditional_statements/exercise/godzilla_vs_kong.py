budged = float(input())
extra = int(input())
clothes_per_extra = float(input())

decor = budged * 0.1
sum_clothes = extra * clothes_per_extra
if extra >= 150:
    sum_clothes -= sum_clothes * 0.1

cost = decor + sum_clothes

if budged >= cost:
    print("Action!")
    print(f"Wingard starts filming with {budged-cost:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {cost - budged:.2f} leva more.")