start = int(input())
final = int(input())
magic_number = int(input())
combination_counter = 0
flag = False

for first_num in range(start, final +1):
    for second_num in range(start, final +1):
        combination_counter += 1
        if first_num + second_num == magic_number:
            flag = True
            print(f"Combination N:{combination_counter} ({first_num} + {second_num} = {magic_number})")
            break
    if flag:
        break
if not flag:
    print(f"{combination_counter} combinations - neither equals {magic_number}")