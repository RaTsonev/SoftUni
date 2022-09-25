budget = float(input())
gpu_num = int(input())
cpu_num = int(input())
ram_num = int(input())

price_gpu = gpu_num*250
price_cpu = price_gpu*0.35*cpu_num
price_ram = price_gpu*0.1*ram_num
price = price_ram + price_gpu + price_cpu
if gpu_num > cpu_num:
    price = price - price*0.15
diff = abs(budget - price)
if budget >= price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")