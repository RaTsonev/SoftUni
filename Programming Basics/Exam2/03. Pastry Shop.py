sweet = input()
sweet_counter = int(input())
day = int(input())
price = 0
if sweet == "Cake":
    if day <= 15:
        price = 24 * sweet_counter
    else:
        price = 28.7 * sweet_counter
elif sweet == "Souffle":
    if day <= 15:
        price = 6.66 * sweet_counter
    else:
        price = 9.80 * sweet_counter
elif sweet == "Baklava":
    if day <= 15:
        price = 12.6 * sweet_counter
    else:
        price = 16.98 * sweet_counter
if day <= 22:
    if 100 <= price <= 200:
        price = price - price * 0.15
    elif price > 200:
        price = price - price * 0.25

if day <= 15:
    price = price - price * 0.1

print(f"{price:.2f}")