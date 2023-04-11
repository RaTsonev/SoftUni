season = input()
kilometers = float(input())
salary = 0

if kilometers <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = kilometers*0.75
    elif season == "Summer":
        salary = kilometers * 0.9
    elif season == "Winter":
        salary = kilometers * 1.05
elif 5000 < kilometers <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = kilometers*0.95
    elif season == "Summer":
        salary = kilometers * 1.1
    elif season == "Winter":
        salary = kilometers * 1.25
elif 10000 < kilometers <= 20000:
        salary = kilometers*1.45
salary = salary*4
salary -= salary*0.1
print(f"{salary:.2f}")