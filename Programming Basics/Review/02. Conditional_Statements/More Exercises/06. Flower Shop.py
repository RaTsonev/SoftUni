import math

magnolias_number = int(input())
hyacinth_number = int(input())
roses_number = int(input())
cactus_number = int(input())
gift_price = float(input())

price_flowers = magnolias_number * 3.25 + hyacinth_number * 4 + roses_number * 3.5 + cactus_number * 8
money = price_flowers - price_flowers*0.05
diff = abs(gift_price-money)
if money >= gift_price:
    diff = math.floor(money-gift_price)
    print(f"She is left with {diff} leva.")
else:
    diff = math.ceil(gift_price - money)
    print(f"She will have to borrow {diff} leva." )