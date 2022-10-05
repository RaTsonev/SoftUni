budget = float(input())
category = input()
people = int(input())

travelling = 0
money_left = ""
if 1 <= people <= 4:
    travelling = budget * 0.75
elif 5 <= people <= 9:
    travelling = budget * 0.6
elif 10 <= people <= 24:
    travelling = budget * 0.5
elif 25 <= people <= 49:
    travelling = budget * 0.4
elif people >= 50:
    travelling = budget * 0.25

if category == "VIP":
    money_left = budget - people * 499.99 - travelling
elif category == "Normal":
    money_left = budget - people * 249.99 - travelling

if money_left >= 0:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_left = abs(money_left)
    print(f"Not enough money! You need {money_left:.2f} leva.")