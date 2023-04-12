x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
myx = float(input())
myy = float(input())

if ((myx == x1 or myx == x2) and (y1 <= myy <= y2)) or ((myy == y1 or myy ==y2) and (x1<= myx <=x2)):
    print("Border")
else:
    print("Inside / Outside")