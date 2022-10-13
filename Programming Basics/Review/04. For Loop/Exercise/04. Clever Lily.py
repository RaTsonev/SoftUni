n_years = int(input())
washing_machine = float(input())
price_doll = int(input())
money = 0
dolls = 0
gave_money = 0
for i in range(1, n_years + 1):
    if i % 2 == 0:
        money += i*5
        gave_money += 1
    else:
        dolls += 1
money_toys = dolls * price_doll
final_money = money - gave_money + money_toys
diff = abs(final_money-washing_machine)
if final_money >= washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")