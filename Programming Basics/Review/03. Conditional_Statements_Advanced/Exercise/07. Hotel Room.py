month = input()
nights = int(input())
studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = nights * 50
    apartment_price = nights * 65
elif month == "June" or month == "September":
    studio_price = nights * 75.20
    apartment_price = nights * 68.70
elif month == "July" or month == "August":
    studio_price = nights * 76
    apartment_price = nights * 77
if nights > 14:
    apartment_price -= apartment_price * 0.1
    if month == "May" or month == "October":
        studio_price = studio_price - studio_price * 0.3
    elif month == "June" or month == "September":
        studio_price -= studio_price * 0.2
elif nights > 7:
    if month == "May" or month == "October":
        studio_price -= studio_price * 0.05
print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")