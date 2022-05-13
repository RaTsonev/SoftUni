import sys

n = int(input())

max_number = -sys.maxsize
sum = 0

for i in range(0,n):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    sum += current_number

sum -= max_number

if sum == max_number:
    print("Yes")
    print(f"Sum = {sum}")
else:
    diff = (abs(sum - max_number))
    print("No")
    print(f"Diff = {diff}")