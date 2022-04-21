price_mackerel_kg = float(input())
price_caca_kg = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = int(input())

price_bonito = price_mackerel_kg +  price_mackerel_kg*0.6
price_horse_mackerel = price_caca_kg + price_caca_kg*0.8
sum= bonito_kg*price_bonito + horse_mackerel_kg*price_horse_mackerel + mussels_kg*7.50
print(f"{sum:.2f}")