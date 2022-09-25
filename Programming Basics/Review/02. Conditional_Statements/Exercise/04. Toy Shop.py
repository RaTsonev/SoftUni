vacation = float(input())
puzzle_number = int(input())
doll_number = int(input())
bear_number = int(input())
minion_number = int(input())
truck_number = int(input())
price = puzzle_number*2.60 + doll_number*3 + bear_number*4.1 + minion_number*8.2 + truck_number*2
counter = puzzle_number+doll_number+bear_number+minion_number+truck_number
if counter >= 50:
    price -= price*0.25
rent = price*0.1
profit = price-rent
diff = abs(vacation-profit)
if profit >= vacation:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")