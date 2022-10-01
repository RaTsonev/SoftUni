town = input()
sells = float(input())
money = 0
if town == "Sofia":
    if sells < 0:
        print("error")
    elif 0 <= sells <= 500:
        money = sells*5/100
        print(f"{money:.2f}")
    elif 500 < sells <= 1000:
        money = sells * 7 / 100
        print(f"{money:.2f}")
    elif 1000 < sells <= 10000:
        money = sells * 8 / 100
        print(f"{money:.2f}")
    elif sells > 10000:
        money = sells * 12 / 100
        print(f"{money:.2f}")
elif town == "Varna":
    if sells < 0:
        print("error")
    elif 0 <= sells <= 500:
        money = sells * 4.5 / 100
        print(f"{money:.2f}")
    elif 500 < sells <= 1000:
        money = sells * 7.5 / 100
        print(f"{money:.2f}")
    elif 1000 < sells <= 10000:
        money = sells * 10 / 100
        print(f"{money:.2f}")
    elif sells > 10000:
        money = sells * 13 / 100
        print(f"{money:.2f}")
elif town == "Plovdiv":
    if sells < 0:
        print("error")
    elif 0 <= sells <= 500:
        money = sells * 5.5 / 100
        print(f"{money:.2f}")
    elif 500 < sells <= 1000:
        money = sells * 8 / 100
        print(f"{money:.2f}")
    elif 1000 < sells <= 10000:
        money = sells * 12 / 100
        print(f"{money:.2f}")
    elif sells > 10000:
        money = sells * 14.5 / 100
        print(f"{money:.2f}")
else:
    print("error")