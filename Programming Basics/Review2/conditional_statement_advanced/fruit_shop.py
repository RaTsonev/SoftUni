fruit = input()
day = input()
quantity = float(input())
working_day = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
weekend = ["Saturday","Sunday"]
fruits = ["banana","apple","orange", "grapefruit","kiwi","pineapple","grapes"]
price = 0
if day not in working_day and day not in weekend or fruit not in fruits:
    print("error")
elif day in working_day:
    if fruit == "banana":
        price = quantity*2.5
    elif fruit == "apple":
        price = quantity*1.2
    elif fruit == "orange":
        price = quantity*0.85
    elif fruit == "grapefruit":
        price = quantity*1.45
    elif fruit == "kiwi":
        price = quantity*2.70
    elif fruit == "pineapple":
        price = quantity*5.50
    elif fruit == "grapes":
        price = quantity*3.85
    print(f"{price:.2f}")
elif day in weekend:
    if fruit == "banana":
        price = quantity * 2.7
    elif fruit == "apple":
        price = quantity * 1.25
    elif fruit == "orange":
        price = quantity * 0.90
    elif fruit == "grapefruit":
        price = quantity * 1.60
    elif fruit == "kiwi":
        price = quantity * 3
    elif fruit == "pineapple":
        price = quantity * 5.60
    elif fruit == "grapes":
        price = quantity * 4.20
    print(f"{price:.2f}")


