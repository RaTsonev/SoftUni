import sys
numbers = int(input())
max_number = -sys.maxsize
sum = 0
for _ in range(1,numbers +1):
    current_number = int(input())
    if current_number >= max_number:
        max_number = current_number
    sum += current_number
sum -= max_number
if max_number == sum:
    print("Yes")
    print(f"Sum = {sum}")
else:
    print("No")
    print(f"Diff = {abs(max_number-sum)}")