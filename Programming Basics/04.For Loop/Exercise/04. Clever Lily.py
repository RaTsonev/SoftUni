lilly_ages = int(input())
washing_machine = float(input())
price_toy = int((input()))

toy_counter = 0
money_given = 0
total_money_saved = 0
for current_ages in range(1, lilly_ages + 1):
    if current_ages % 2 != 0:
        toy_counter += 1
    else:
        money_given = (current_ages * 5) - 1
        total_money_saved += money_given

sell_toy = price_toy * toy_counter
total_money_saved += sell_toy
diff = abs(total_money_saved - washing_machine)
if total_money_saved >= washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")