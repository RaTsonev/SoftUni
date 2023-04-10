type_flower = input()
quantity_flowers = int(input())
budged = int(input())
cost = 0
if type_flower == "Roses":
    cost = quantity_flowers*5
    if quantity_flowers > 80:
        cost -= cost*0.1
elif type_flower == "Dahlias":
    cost = quantity_flowers*3.80
    if quantity_flowers > 90:
        cost -= cost*0.15
elif type_flower == "Tulips":
    cost = quantity_flowers*2.80
    if quantity_flowers > 80:
        cost -= cost*0.15
elif type_flower == "Narcissus":
    cost = quantity_flowers*3
    if quantity_flowers < 120:
        cost += cost*0.15
elif type_flower == "Gladiolus":
    cost = quantity_flowers*2.5
    if quantity_flowers < 80:
        cost += cost*0.2
if budged >= cost:
    print(f"Hey, you have a great garden with {quantity_flowers} {type_flower} and {budged-cost:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(cost-budged):.2f} leva more.")