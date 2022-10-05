season = input()
group = input()
number_students = int(input())
nights = int(input())
sport = ""
price = 0
if group == "girls":
    if season == "Winter":
        sport = "Gymnastics"
        price = number_students * nights * 9.60
    elif season == "Spring":
        sport = "Athletics"
        price = number_students * nights * 7.20
    elif season == "Summer":
        sport = "Volleyball"
        price = number_students * nights * 15
elif group == "boys":
    if season == "Winter":
        sport = "Judo"
        price = number_students * nights * 9.60
    elif season == "Spring":
        sport = "Tennis"
        price = number_students * nights * 7.20
    elif season == "Summer":
        sport = "Football"
        price = number_students * nights * 15
elif group == "mixed":
    if season == "Winter":
        sport = "Ski"
        price = number_students * nights * 10
    elif season == "Spring":
        sport = "Cycling"
        price = number_students * nights * 9.50
    elif season == "Summer":
        sport = "Swimming"
        price = number_students * nights * 20

if number_students >= 50:
    price -= price * 0.5
elif 20 <= number_students < 50:
    price -= price * 0.15
elif 10 <= number_students < 20:
    price -= price * 0.05
print(f"{sport} {price:.2f} lv.")