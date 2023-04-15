budget = float(input())
season = input()
type = ""
cabrio = 0
jeep = 0
if season == "Summer" and budget <= 500:
    if budget <= 100:
        type = "Economy class"
        cabrio = budget * 0.35
    elif 100< budget <= 500:
        type = "Compact class"
        cabrio = budget * 0.45
    print(f"{type}")
    print(f"Cabrio - {cabrio:.2f}")
elif season == "Winter" and budget <= 500:
    if budget <= 100:
        type = "Economy class"
        jeep = budget * 0.65
    elif 100< budget <= 500:
        type = "Compact class"
        jeep = budget * 0.8
    print(f"{type}")
    print(f"Jeep - {jeep:.2f}")
if budget > 500:
    type = "Luxury class"
    jeep = budget * 0.9
    print(f"{type}")
    print(f"Jeep - {jeep:.2f}")