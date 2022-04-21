degree = float(input())
if 26 <= degree and degree <= 35:
    print("Hot")
if 20.1 <= degree and degree <= 25.9:
    print("Warm")
if 15.00 <= degree and degree <= 20.00:
    print("Mild")
if 12.00 <= degree and degree <= 14.9:
    print("Cool")
if 5.00 <= degree and degree <= 11.9:
    print("Cold")
if degree < 5.00:
    print("unknown")
if degree > 35.00:
    print("unknown")
