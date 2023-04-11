budged = float(input())
season = input()
location = ""
place = ""
sum = 0
if season == "Summer":
    if budged <= 1000:
        place = "Camp"
        location = "Alaska"
        sum = budged*0.65
    elif 1000<= budged <= 3000:
        place = "Hut"
        location = "Alaska"
        sum = budged*0.8
    elif budged > 3000:
        place = "Hotel"
        location = "Alaska"
        sum = budged*0.9
elif season == "Winter":
    if budged <= 1000:
        place = "Camp"
        location = "Morocco"
        sum = budged*0.45
    elif 1000<= budged <= 3000:
        place = "Hut"
        location = "Morocco"
        sum = budged*0.6
    elif budged > 3000:
        place = "Hotel"
        location = "Morocco"
        sum = budged*0.9
print(f"{location} - {place} - {sum:.2f}")