budget = float(input())
gpu_num = int(input())
cpu_num = int(input())
ram_num = int(input())

gpu_price = gpu_num*250
price = gpu_price + cpu_num*gpu_price*0.35 + ram_num*gpu_price*0.1
if gpu_num > cpu_num:
    price = price-(price*0.15)

if budget >= price:
    money_left = budget - price
    print(f"You have {money_left:.2f} leva left!")
else:
    money_left = price - budget
    print(f"Not enough money! You need {money_left:.2f} leva more!")
