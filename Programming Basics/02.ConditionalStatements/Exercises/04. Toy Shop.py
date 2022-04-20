price_vacantion = float(input())
num_puzzle = int(input())
num_doll = int(input())
num_bear = int(input())
num_minions = int(input())
num_truck = int(input())

discount = 0
price_puzzle = num_puzzle*2.60
price_doll = num_doll*3
price_bear = num_bear*4.10
price_minions = num_minions*8.20
price_truck = num_truck*2

num_toys = num_puzzle + num_doll + num_bear + num_minions + num_truck
price = price_puzzle + price_doll + price_bear + price_minions + price_truck

if num_toys >= 50:
    discount = price*0.25

price_with_discount = price - discount
rent = price_with_discount*0.1
final_price = price_with_discount - rent

if price_vacantion <= final_price:
    money_left = final_price - price_vacantion
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_left = abs(final_price-price_vacantion)
    print(f"Not enough money! {money_left:.2f} lv needed.")