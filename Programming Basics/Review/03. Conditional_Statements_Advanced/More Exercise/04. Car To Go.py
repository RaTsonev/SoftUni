budget = float(input())
season = input()
rating = ""
car = ""
price = 0
if budget <= 100:
    rating = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        price = budget*0.35
    elif season == "Winter":
        car = "Jeep"
        price = budget*0.65
elif 100 < budget <= 500:
    rating = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        price = budget*0.45
    elif season == "Winter":
        car = "Jeep"
        price = budget*0.80
if budget > 500:
    rating = "Luxury class"
    car = "Jeep"
    price = budget*0.90

print(f"{rating}")
print(f"{car} - {price:.2f}")