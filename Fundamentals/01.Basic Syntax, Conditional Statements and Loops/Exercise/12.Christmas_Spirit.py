quantity_of_decoration = int(input())
days_left_christmas = int(input())
cost = 0
spirit = 0
for current_day in range(1, days_left_christmas + 1):
    if current_day % 11 == 0:
        quantity_of_decoration += 2
    if current_day % 2 == 0:
        cost += quantity_of_decoration * 2
        spirit += 5
    if current_day % 3 == 0:
        cost += quantity_of_decoration * (5 + 3)
        spirit += 10 + 3
    if current_day % 5 == 0:
        cost += quantity_of_decoration * 15
        spirit += 17
        if current_day % 3 == 0:
            spirit += 30
    if current_day % 10 == 0:
        spirit -= 20
        cost += 5 + 3 + 15
if days_left_christmas % 10 == 0:
    spirit -= 30
print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")