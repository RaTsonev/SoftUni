holiday = float(input())
puzzle = int(input())
doll = int(input())
bear = int(input())
minion = int(input())
truck = int(input())

sum_puzzle = puzzle * 2.6
sum_doll = doll * 3
sum_bear = bear * 4.1
sum_minion = minion * 8.2
sum_truck = truck * 2

order = puzzle + doll + bear + minion + truck
sum_order = sum_puzzle + sum_doll + sum_bear + sum_minion + sum_truck

if order >= 50:
    sum_order -= sum_order * 0.25

sum_order -= sum_order * 0.1

if sum_order >= holiday:
    print(f"Yes! {sum_order-holiday:.2f} lv left.")
else:
    print(f"Not enough money! {holiday-sum_order:.2f} lv needed.")