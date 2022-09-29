fuel = input()
litres = float(input())
card = input()
price = 0
if card == "Yes":
    if fuel == "Gasoline":
        price = litres * 2.04
    elif fuel == "Diesel":
        price = litres * 2.21
    elif fuel == "Gas":
        price = litres * 0.85
else:
    if fuel == "Gasoline":
        price = litres * 2.22
    elif fuel == "Diesel":
        price = litres * 2.33
    elif fuel == "Gas":
        price = litres * 0.93

if 20 <= litres <= 25:
    price = price - price*0.08
elif litres > 25:
    price = price - price * 0.1

print(f"{price:.2f} lv.")