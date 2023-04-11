type_holiday = input()
type_group = input()
students = int(input())
nights = int(input())
sleeping = 0
sport = ""
if type_holiday == "Winter":
    if type_group == "girls":
        sport = "Gymnastics"
        sleeping = nights * students * 9.6
    elif type_group == "boys":
        sport = "Judo"
        sleeping = nights*students *9.6
    elif type_group == "mixed":
        sport = "Ski"
        sleeping = nights*students *10
elif type_holiday == "Spring":
    if type_group == "girls":
        sport = "Athletics"
        sleeping = nights * students *7.2
    elif type_group == "boys":
        sport = "Tennis"
        sleeping = nights*students *7.2
    elif type_group == "mixed":
        sport = "Cycling"
        sleeping = nights*students *9.5
elif type_holiday == "Summer":
    if type_group == "girls":
        sport = "Volleyball"
        sleeping = nights *students * 15
    if type_group == "boys":
        sport = "Football"
        sleeping = nights*students *15
    elif type_group == "mixed":
        sport = "Swimming"
        sleeping = nights*students *20
if students >= 50:
    sleeping -= sleeping*0.5
elif students >= 20:
    sleeping -= sleeping * 0.15
elif students >= 10:
    sleeping -= sleeping * 0.05
print(f"{sport} {sleeping:.2f} lv.")
