from math import pi
shape = input()
area = 0
if shape == "square":
    a = float(input())
    area = a*a
if shape == "rectangle":
    a = float(input())
    b = float(input())
    area = a*b
if shape == "circle":
    r = float(input())
    area = pi*r*r
if shape == "triangle":
    a = float(input())
    h = float(input())
    area = a*h/2
print(f"{area:.3f}")