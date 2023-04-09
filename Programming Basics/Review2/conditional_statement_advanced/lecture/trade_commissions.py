city = input()
sales = float(input())
commission = 0
towns = ["Sofia","Varna","Plovdiv"]
if city not in towns or 0 > sales:
    print("error")
else:
    if 0 <= sales <= 500:
        if city == "Sofia":
            commission = sales * 0.05
        elif city == "Varna":
            commission = sales * 0.045
        elif city == "Plovdiv":
            commission = sales * 0.055
        print(f"{commission:.2f}")
    elif 500 < sales <= 1000:
        if city == "Sofia":
            commission = sales * 0.07
        elif city == "Varna":
            commission = sales * 0.075
        elif city == "Plovdiv":
            commission = sales * 0.08
        print(f"{commission:.2f}")
    elif 1000 < sales <= 10000:
        if city == "Sofia":
            commission = sales * 0.08
        elif city == "Varna":
            commission = sales * 0.1
        elif city == "Plovdiv":
            commission = sales * 0.12
        print(f"{commission:.2f}")
    elif sales > 10000:
        if city == "Sofia":
            commission = sales * 0.12
        elif city == "Varna":
            commission = sales * 0.13
        elif city == "Plovdiv":
            commission = sales * 0.145
        print(f"{commission:.2f}")
