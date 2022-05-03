budget = float(input())
season = input()

cost = 0
destination = ""
type_journey = ""
if budget <= 100:
    if season == "summer":
        cost = budget * 0.3
        type_journey = "Camp"
    else:
        cost = budget*0.7
        type_journey = "Hotel"
    destination = "Bulgaria"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        cost = budget * 0.4
        type_journey = "Camp"
    else:
        cost = budget * 0.8
        type_journey = "Hotel"
elif budget > 1000:
    destination = "Europe"
    cost = budget*0.9
    type_journey = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_journey} - {cost:.2f}")