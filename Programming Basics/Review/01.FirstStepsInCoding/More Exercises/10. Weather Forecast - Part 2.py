degrees = float(input())
if 26.00 <= degrees <= 35.00:
    print("Hot")
elif 20.1 <= degrees <= 25.9:
    print("Warm")
elif 15.00 <= degrees <= 20.00:
    print("Mild")
elif 12.00 <= degrees <= 14.99:
    print("Cool")
elif 5 <= degrees <= 11.9:
    print("Cold")
else:
    print("unknown")