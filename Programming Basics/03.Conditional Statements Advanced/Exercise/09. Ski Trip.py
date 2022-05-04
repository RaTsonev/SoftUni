days = int(input())
place = input()
rating = input()

final_price = 0
if days < 10:
    if place == "room for one person":
        final_price = (days - 1)*18
    elif place == "apartment":
        final_price = (days-1)*25 - (days-1)*25*0.3
    elif place == "president apartment":
        final_price = (days-1)*35 - (days-1)*35*0.1
elif 10 <= days <= 15:
    if place == "room for one person":
        final_price = (days - 1)*18
    elif place == "apartment":
        final_price = (days-1)*25 - (days-1)*25*0.35
    elif place == "president apartment":
        final_price = (days-1)*35 - (days-1)*35*0.15
if days > 15:
    if place == "room for one person":
        final_price = (days - 1)*18
    elif place == "apartment":
        final_price = (days-1)*25 - (days-1)*25*0.5
    elif place == "president apartment":
        final_price = (days-1)*35 - (days-1)*35*0.2

if rating == "positive":
    final = final_price + final_price*0.25
    print(f"{final:.2f}")
else:
    final = final_price - final_price*0.1
    print(f"{final:.2f}")