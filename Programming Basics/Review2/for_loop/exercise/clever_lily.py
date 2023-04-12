years = int(input())
washing_machine = float(input())
price_toy = int(input())
toys = 0
money = 0
taken = 0
for age in range(1,years + 1):
    if age % 2 == 0:
        money += age*5
        taken += 1
    else:
        toys += 1
earned = money + toys*price_toy - taken
if earned >= washing_machine:
    print(f"Yes! {earned-washing_machine:.2f}")
else:
    print(f"No! {washing_machine-earned:.2f}")