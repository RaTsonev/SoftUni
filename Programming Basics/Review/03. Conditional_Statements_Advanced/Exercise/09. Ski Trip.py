days = int(input())
room = input()
rating = input()

nights = days - 1
price = 0

if room == "room for one person":
    price = nights * 18
elif room == "apartment":
    if days < 10:
        price = nights * 25 - nights * 25 * 0.3
    elif 10 < days < 15:
        price = nights * 25 - nights * 25 * 0.35
    elif days > 15:
        price = nights * 25 - nights * 25 * 0.5
elif room == "president apartment":
    if days < 10:
        price = nights * 35 - nights * 35 * 0.1
    elif 10 < days < 15:
        price = nights * 35 - nights * 35 * 0.15
    elif days > 15:
        price = nights * 35 - nights * 35 * 0.20

if rating == "positive":
    price += price * 0.25
else:
    price -= price * 0.1
print(f"{price:.2f}")