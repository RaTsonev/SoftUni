season = input()
kilometers = float(input())
money = 0
if kilometers <= 5000:
    if season == "Spring" or season == "Autumn":
        money = kilometers * 0.75
    elif season == "Summer":
        money = kilometers * 0.90
    elif season == "Winter":
        money = kilometers * 1.05
elif 5000 < kilometers <= 10000:
    if season == "Spring" or season == "Autumn":
        money = kilometers * 0.95
    elif season == "Summer":
        money = kilometers * 1.10
    elif season == "Winter":
        money = kilometers * 1.25
elif 10000 < kilometers <= 20000:
    money = kilometers * 1.45
money = money * 4
money -= money * 0.1
print(f"{money:.2f}")