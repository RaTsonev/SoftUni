months = int(input())
sum_electricity = 0
sum_water = 0
sum_internet = 0
sum_other = 0
for _ in range(1, months + 1):
    electricity = float(input())
    sum_electricity += electricity
    sum_other += electricity + 20 + 15 + (electricity + 20 + 15) * 0.2
sum_water = months * 20
sum_internet = months * 15

average = (sum_electricity + sum_water + sum_internet + sum_other) / months
print(f"Electricity: {sum_electricity:.2f} lv")
print(f"Water: {sum_water:.2f} lv")
print(f"Internet: {sum_internet:.2f} lv")
print(f"Other: {sum_other:.2f} lv")
print(f"Average: {average:.2f} lv")