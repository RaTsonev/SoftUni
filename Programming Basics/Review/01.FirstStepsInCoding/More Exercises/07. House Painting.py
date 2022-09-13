x = float(input())
y = float(input())
h = float(input())
wall = 2*x*x - 1.2*2 + 2*x*y - 1.5*1.5*2
paint_wall = wall/3.4
roof = 2*x*y + 2*x*h/2
paint_roof = roof/4.3
print(f"{paint_wall:.2f}")
print(f"{paint_roof:.2f}")
