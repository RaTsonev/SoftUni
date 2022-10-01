projection = input()
row = int(input())
column = int(input())
money = 0
if projection == "Premiere":
    money = row*column*12
elif projection == "Normal":
    money = row*column*7.50
elif projection == "Discount":
    money = row*column*5
print(f"{money:.2f} leva")