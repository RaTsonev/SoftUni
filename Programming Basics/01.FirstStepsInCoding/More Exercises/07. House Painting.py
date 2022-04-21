height = float(input())
length = float(input())
h_roof = float(input())

side1 = 2*height*height - 1.2*2
side2 = 2*height*length - 1.5*1.5*2
paint_green = (side1+side2)/3.4

roof1 = height*length
roof2 = height*h_roof/2
paint_red = (2*roof1+2*roof2)/4.3

print(f"{paint_green:.2f}")
print(f"{paint_red:.2f}")