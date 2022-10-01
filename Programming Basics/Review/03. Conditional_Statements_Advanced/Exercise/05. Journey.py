budget = float(input())
season = input()
destination = ""
place = ""
price = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        price = 0.3 * budget
    elif season == "winter":
        place = "Hotel"
        price = 0.7 * budget
if 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        price = 0.4 * budget
    elif season == "winter":
        place = "Hotel"
        price = 0.8 * budget
if budget > 1000:
    destination = "Europe"
    place = "Hotel"
    price = 0.9*budget
print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")