number = int(input())
sum = 0
current_num = int(input())
while True:
    sum += current_num
    if sum >= number:
        print(sum)
        break
    current_num = int(input())