import math
square = "square"
rectangle = "rectangle"
circle = "circle"
triangle = "triangle"
figure = input("")
if figure == square:
    side = float(input())
    area = side*side
    print(f"{area:.3f}")
if figure == rectangle:
    side1 = float(input())
    side2 = float(input())
    area= side1*side2
    print(f"{area:.3f}")
if figure == circle:
    radius = float(input())
    area = math.pi * radius * radius
    print(f"{area:.3f}")
if figure == triangle:
    side = float(input())
    height = float(input())
    area = (side * height)/2
    print(f"{area:.3f}")
