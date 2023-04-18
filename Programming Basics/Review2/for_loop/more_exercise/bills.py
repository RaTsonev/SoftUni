months = int(input())
sum_electricity = 0
sum_other = 0
for _ in range(months):
    electricity = float(input())
    sum_electricity += electricity
    sum_other += electricity + 20 + 15 + (electricity + 20 + 15)*0.2

print(f"Electricity: {sum_electricity:.2f} lv")
print(f"Water: {months*20:.2f} lv")
print(f"Internet: {months*15:.2f} lv")
print(f"Other: {sum_other:.2f} lv")
print(f"Average: {(sum_electricity+months*20+months*15+sum_other)/months:.2f} lv")