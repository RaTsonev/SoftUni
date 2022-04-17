budget = float(input())
extras = int(input())
price_clothing_person = float(input())
price_clothing = price_clothing_person*extras
decor = budget*0.1
if extras > 150:
    price_clothing -= price_clothing*0.1

final_price = decor + price_clothing

if final_price > budget:
    price = abs(final_price-budget)
    print(f"Not enough money!\n Wingard needs {price:.2f} leva more.")
else:
    price = budget - final_price
    print(f"Action!\n Wingard starts filming with {price:.2f} leva left.")


