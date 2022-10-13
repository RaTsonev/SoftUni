import sys

n = int(input())
max_num = -sys.maxsize
sum = 0
for i in range(0, n):
    current_number = int(input())
    if current_number > max_num:
        max_num = current_number
    sum += current_number
total = sum - max_num
if total == max_num:
    print("Yes")
    print(f"Sum = {total}")
else:
    diff = abs(total-max_num)
    print("No")
    print(f"Diff = {diff}")