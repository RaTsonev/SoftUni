budged = float(input())
season = input()
type = ""
cabrio = 0
jeep = 0
if season == "Summer" and budged <= 500:
    if budged <= 100:
        type = "Economy class"
        cabrio = budged*0.35
    elif 100< budged <= 500:
        type = "Compact class"
        cabrio = budged*0.45
    print(f"{type}")
    print(f"Cabrio - {cabrio:.2f}")
elif season == "Winter" and budged <= 500:
    if budged <= 100:
        type = "Economy class"
        jeep = budged * 0.65
    elif 100< budged <= 500:
        type = "Compact class"
        jeep = budged * 0.8
    print(f"{type}")
    print(f"Jeep - {jeep:.2f}")
if budged > 500:
    type = "Luxury class"
    jeep = budged * 0.9
    print(f"{type}")
    print(f"Jeep - {jeep:.2f}")