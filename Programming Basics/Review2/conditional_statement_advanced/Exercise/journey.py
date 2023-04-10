budged = float(input())
season = input()
cost = 0
destination = ""
sleeping = ""
if budged <= 100:
    destination = "Bulgaria"
    if season == "summer":
        sleeping = "Camp"
        cost = budged*0.3
    else:
        sleeping = "Hotel"
        cost = budged*0.7
elif budged <= 1000:
    destination = "Balkans"
    if season == "summer":
        sleeping = "Camp"
        cost = budged*0.4
    else:
        sleeping = "Hotel"
        cost = budged*0.8
elif budged > 1000:
    destination = "Europe"
    sleeping = "Hotel"
    cost = budged*0.9
print(f"Somewhere in {destination}")
print(f"{sleeping} - {cost:.2f}")