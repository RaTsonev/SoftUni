n = int(input())
sum = 0
times = 0
for _ in range (n):
    number = int(input())
    sum += number
    times += 1
result = sum/times
print(f"{result:.2f}")