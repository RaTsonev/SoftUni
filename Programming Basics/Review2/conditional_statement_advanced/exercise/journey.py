budget = float(input())
season = input()
cost = 0
destination = ""
sleeping = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        sleeping = "Camp"
        cost = budget * 0.3
    else:
        sleeping = "Hotel"
        cost = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        sleeping = "Camp"
        cost = budget * 0.4
    else:
        sleeping = "Hotel"
        cost = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    sleeping = "Hotel"
    cost = budget * 0.9
print(f"Somewhere in {destination}")
print(f"{sleeping} - {cost:.2f}")