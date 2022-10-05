number_chrysanthemum = int(input())
number_roses = int(input())
number_tulip = int(input())
season = input()
day = input()
price = 0
flowers = number_chrysanthemum + number_roses + number_tulip
if season == "Spring" or season == "Summer":
        price = number_chrysanthemum * 2 + number_roses * 4.1 + number_tulip * 2.5
elif season == "Autumn" or season == "Winter":
        price = number_chrysanthemum * 3.75 + number_roses * 4.5 + number_tulip * 4.15

if day == "Y":
    price += price*0.15
elif day == "N":
    price = price
if number_tulip >= 7 and season == "Spring":
    price -= price*0.05
elif number_roses >= 10 and season == "Winter":
    price -= price * 0.1
if flowers >= 20:
    price -= price * 0.2
price += 2
print(f"{price:.2f}")