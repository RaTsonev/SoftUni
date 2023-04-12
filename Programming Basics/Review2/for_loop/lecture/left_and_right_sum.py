n = int(input())
right_sum = 0
left_sum = 0
for _ in range(1,n+1):
    right_sum += int(input())
for _ in range(1,n+1):
    left_sum += int(input())

if right_sum == left_sum:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {abs(right_sum-left_sum)}")