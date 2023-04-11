month = input()
nights = int(input())
studio = 0
apartment = 0
if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 14 >= nights > 7:
        studio -= studio*0.05
    elif nights > 14:
        studio -= studio*0.3
        apartment -= apartment*0.1
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if nights > 14:
        studio -= studio*0.2
        apartment -= apartment * 0.1
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if nights > 14:
        apartment -= apartment * 0.1
price_studio = studio*nights
price_apartment = apartment*nights
print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")