month = input()
nights = int(input())

studio = 0
apartament = 0
if month == "May" or month == "October":
    apartament = nights*65
    studio = nights*50
    if 14 > nights > 7:
        studio = studio - studio*0.05
    elif nights > 14:
        studio = studio - studio*0.30
        apartament = apartament - apartament*0.1
elif month == "June" or month == "September":
    apartament = nights * 68.70
    studio = nights * 75.20
    if nights > 14:
        studio = studio - studio*0.20
        apartament = apartament - apartament * 0.1
elif month == "July" or month == "August":
    apartament = nights * 77
    studio = nights * 76
    if nights > 14:
        apartament = apartament - apartament * 0.1

print(f"Apartment: {apartament:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")
