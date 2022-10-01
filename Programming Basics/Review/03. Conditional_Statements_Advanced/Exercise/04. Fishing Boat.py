budget = int(input())
season = input()
fishers = int(input())
boat = 0
if season == "Spring":
    if fishers <= 6:
        boat = 3000 - 3000 * 0.1
    elif 7 <= fishers <= 11:
        boat = 3000 - 3000 * 0.15
    elif fishers >= 12:
        boat = 3000 - 3000 * 0.25
elif season == "Summer":
    if fishers <= 6:
        boat = 4200 - 4200 * 0.1
    elif 7 <= fishers <= 11:
        boat = 4200 - 4200 * 0.15
    elif fishers >= 12:
        boat = 4200 - 4200 * 0.25
elif season == "Autumn":
    if fishers <= 6:
        boat = 4200 - 4200 * 0.1
    elif 7 <= fishers <= 11:
        boat = 4200 - 4200 * 0.15
    elif fishers >= 12:
        boat = 4200 - 4200 * 0.25
elif season == "Winter":
    if fishers <= 6:
        boat = 2600 - 2600 * 0.1
    elif 7 <= fishers <= 11:
        boat = 2600 - 2600 * 0.15
    elif fishers >= 12:
        boat = 2600 - 2600 * 0.25

if fishers % 2 == 0 and season != "Autumn":
    boat -= boat*0.05
diff = abs(budget - boat)
if budget >= boat:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")