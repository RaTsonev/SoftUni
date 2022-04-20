import math
w = float(input())
h = float(input())

if 3<=h<=w<=100:
    one_place=0.7*1.20
    width = math.floor((h-1)/0.7)
    height = math.floor(w/1.2)
    neshto = width*height - 3
    print(f"{neshto}")