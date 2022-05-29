max_number = int(input())
sum = 0
while True:
    current_num = int(input())
    sum += current_num
    if sum >= max_number:
        print(sum)
        break
