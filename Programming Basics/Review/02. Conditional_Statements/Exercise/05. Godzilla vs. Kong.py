budget = float(input())
extra_number = int(input())
price_cloth_extra = float(input())
cloth = 0
decor = budget*0.1

if extra_number > 150:
    cloth = (price_cloth_extra - price_cloth_extra*0.1)*extra_number
else:
    cloth = price_cloth_extra*extra_number
price = decor + cloth
diff = abs(price - budget)
if budget >= price:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")