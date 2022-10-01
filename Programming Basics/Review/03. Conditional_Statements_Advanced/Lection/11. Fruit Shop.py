fruit = input()
day = input()
amount = float(input())

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        bill = amount*2.50
        print(f"{bill:.2f}")
    elif fruit == "apple":
        bill = amount*1.20
        print(f"{bill:.2f}")
    elif fruit == "orange":
        bill = amount*0.85
        print(f"{bill:.2f}")
    elif fruit == "grapefruit":
        bill = amount*1.45
        print(f"{bill:.2f}")
    elif fruit == "kiwi":
        bill = amount*2.70
        print(f"{bill:.2f}")
    elif fruit == "pineapple":
        bill= amount*5.50
        print(f"{bill:.2f}")
    elif fruit == "grapes":
        bill = amount*3.85
        print(f"{bill:.2f}")
    else:
        print("error")
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        bill = amount*2.70
        print(f"{bill:.2f}")
    elif fruit == "apple":
        bill = amount*1.25
        print(f"{bill:.2f}")
    elif fruit == "orange":
        bill = amount*0.90
        print(f"{bill:.2f}")
    elif fruit == "grapefruit":
        bill = amount*1.60
        print(f"{bill:.2f}")
    elif fruit == "kiwi":
        bill = amount*3
        print(f"{bill:.2f}")
    elif fruit == "pineapple":
        bill = amount*5.60
        print(f"{bill:.2f}")
    elif fruit == "grapes":
        bill = amount*4.20
        print(f"{bill:.2f}")
    else:
        print("error")
else:
    print("error")