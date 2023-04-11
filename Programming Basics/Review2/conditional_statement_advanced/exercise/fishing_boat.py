budged = int(input())
season = input()
fishers = int(input())
cost = 0
if season == "Spring":
    cost = 3000
elif season == "Summer":
    cost = 4200
elif season == "Autumn":
    cost = 4200
elif season == "Winter":
    cost = 2600

if fishers <= 6:
    cost -= cost*0.1
elif 7 <= fishers <= 11:
    cost -= cost*0.15
if fishers > 12:
    cost -= cost*0.25

if fishers % 2 == 0 and season != "Autumn":
    cost -= cost*0.05
if budged >= cost:
    print(f"Yes! You have {budged-cost:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(cost-budged):.2f} leva.")