product = input()
city = input()
quantity = float(input())
sum = 0
if product == "coffee":
    if city == "Sofia":
        sum = quantity*0.5
    elif city == "Plovdiv":
        sum = quantity*0.4
    elif city == "Varna":
        sum = quantity*0.45
elif product == "water":
    if city == "Sofia":
        sum = quantity*0.8
    elif city == "Plovdiv" or city == "Varna":
        sum = quantity*0.7
elif product == "beer":
    if city == "Sofia":
        sum = quantity*1.2
    elif city == "Plovdiv":
        sum = quantity*1.15
    elif city == "Varna":
        sum = quantity*1.1
if product == "sweets":
    if city == "Sofia":
        sum = quantity*1.45
    elif city == "Plovdiv":
        sum = quantity*1.30
    elif city == "Varna":
        sum = quantity*1.35
if product == "peanuts":
    if city == "Sofia":
        sum = quantity*1.60
    elif city == "Plovdiv":
        sum = quantity*1.50
    elif city == "Varna":
        sum = quantity*1.55
print(sum)