budget = float(input())
category = input()
people = int(input())
tickets = 0
transport = 0
if category == "VIP":
    tickets = people * 499.99
elif category == "Normal":
    tickets = people * 249.99
if 1 <= people <= 4:
    transport = budget * 0.75
elif 5 <= people <= 9:
    transport = budget * 0.6
elif 10 <= people <= 24:
    transport = budget * 0.5
elif 25 <= people <= 49:
    transport = budget * 0.4
elif people >= 50:
    transport = budget * 0.25
diff = abs(budget - transport)
if diff >= tickets:
    print(f"Yes! You have {diff-tickets:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(diff-tickets):.2f} leva.")