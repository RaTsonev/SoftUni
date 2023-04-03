budged = float(input())
gpu_number = int(input())
cpu_number = int(input())
ram_number = int(input())

sum_gpu = gpu_number * 250
sum_cpu = cpu_number * sum_gpu * 0.35
sum_ram = ram_number * sum_gpu * 0.1
final_sum = sum_gpu + sum_cpu + sum_ram
if gpu_number > cpu_number:
    final_sum -= final_sum*0.15
if budged >= final_sum:
    print(f"You have {budged-final_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {final_sum-budged:.2f} leva more!")
