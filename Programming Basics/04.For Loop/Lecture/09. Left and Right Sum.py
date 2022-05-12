num = int(input())
count = 2*num
sum_left = 0
sum_right = 0

for i in range(1,num+1):
    sum_left = sum_left + int(input())

for j in range(1, num+1):
    sum_right = sum_right + int(input())

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    diff = abs(sum_right - sum_left)
    print(f"No, diff = {diff}")