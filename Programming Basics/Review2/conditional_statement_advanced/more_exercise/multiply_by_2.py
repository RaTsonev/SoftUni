number = float(input())

while True:
    if number >= 0:
     result = number*2
     print(f"Result: {result:.2f}")
     number = float(input())
    else:
        print("Negative number!")
        break