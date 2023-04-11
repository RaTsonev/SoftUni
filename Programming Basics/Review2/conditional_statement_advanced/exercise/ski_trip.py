days = int(input())
premises = input()
rating = input()
cost = 0
if days < 10:
    if premises == "room for one person":
        cost = (days - 1)*18
    elif premises == "apartment":
        cost = (days - 1)*25 - (days - 1)*25*0.3
    elif premises == "president apartment":
        cost = (days - 1)*35 - (days - 1)*35*0.1
elif 10 <= days <= 15:
    if premises == "room for one person":
        cost = (days - 1) * 18
    elif premises == "apartment":
        cost = (days - 1) * 25 - (days - 1) * 25 * 0.35
    elif premises == "president apartment":
        cost = (days - 1) * 35 - (days - 1) * 35 * 0.15
elif days > 15:
    if premises == "room for one person":
        cost = (days - 1) * 18
    elif premises == "apartment":
        cost = (days - 1) * 25 - (days - 1) * 25 * 0.5
    elif premises == "president apartment":
        cost = (days - 1) * 35 - (days - 1) * 35 * 0.2

if rating == "positive":
    cost += cost*0.25
elif rating == "negative":
    cost -= cost * 0.1
print(f"{cost:.2f}")