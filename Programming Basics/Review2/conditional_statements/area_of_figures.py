import math
figure = input()
area = 0
if figure == "square":
    side = float(input())
    area = side*side
if figure == "rectangle":
    side1 = float(input())
    side2 = float(input())
    area = side1 * side2
if figure == "circle":
    radius = float(input())
    area = math.pi * radius*radius
if figure == "triangle":
    side = float(input())
    height = float(input())
    area = (side * height)/2
print(f"{area:.3f}")