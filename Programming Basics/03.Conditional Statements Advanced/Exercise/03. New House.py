type_flower = input()
counter_flower = int(input())
budget = int(input())

roses = 0
dahlias = 0
tulips = 0
narcissus = 0
gladiolus = 0
price = 0

if type_flower == "Roses":
   if counter_flower > 80:
       price = counter_flower*5 - counter_flower*5*0.1
   else:
       price = counter_flower*5

elif type_flower == "Tulips":
    if counter_flower > 80:
        price = counter_flower * 2.8 - counter_flower * 2.8 * 0.15
    else:
        price = counter_flower * 2.8

elif type_flower == "Dahlias":
    if counter_flower > 90:
        price = counter_flower * 3.8 - counter_flower * 3.8 * 0.15
    else:
        price = counter_flower * 3.8

elif type_flower == "Narcissus":
    if counter_flower < 120:
        price = counter_flower * 3 + counter_flower * 3 * 0.15
    else:
        price = counter_flower * 3

elif type_flower == "Gladiolus":
    if counter_flower < 80:
        price = counter_flower * 2.5 + counter_flower * 2.5 * 0.2
    else:
        price = counter_flower * 2.5

if budget >= price:
    diff = budget - price
    print(f"Hey, you have a great garden with {counter_flower} {type_flower} and {diff:.2f} leva left.")
else:
    diff = price - budget
    print(f"Not enough money, you need {diff:.2f} leva more.")
