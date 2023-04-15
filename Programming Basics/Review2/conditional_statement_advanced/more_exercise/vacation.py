budget = float(input())
season = input()
location = ""
place = ""
sum = 0
if season == "Summer":
    if budget <= 1000:
        place = "Camp"
        location = "Alaska"
        sum = budget * 0.65
    elif 1000<= budget <= 3000:
        place = "Hut"
        location = "Alaska"
        sum = budget * 0.8
    elif budget > 3000:
        place = "Hotel"
        location = "Alaska"
        sum = budget * 0.9
elif season == "Winter":
    if budget <= 1000:
        place = "Camp"
        location = "Morocco"
        sum = budget * 0.45
    elif 1000<= budget <= 3000:
        place = "Hut"
        location = "Morocco"
        sum = budget * 0.6
    elif budget > 3000:
        place = "Hotel"
        location = "Morocco"
        sum = budget * 0.9
print(f"{location} - {place} - {sum:.2f}")