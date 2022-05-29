people = int(input())
season = input()
price = 0
final_price = 0

if season == "spring":
    if people <= 5:
        price = people*50
    elif people > 5:
        price = people*48
elif season == "summer":
    if people <= 5:
        price = people*48.5
        price = price - (price * 0.15)
    elif people > 5:
        price = people*45
        price = price - (price * 0.15)
elif season == "autumn":
    if people <= 5:
        price = people*60
    elif people > 5:
        price = people*49.5
elif season == "winter":
    if people <= 5:
        price = people*86
        price = price + (price * 0.08)
    elif people > 5:
        price = people*85
        price = price + (price * 0.08)

print(f"{price:.2f} leva.")

