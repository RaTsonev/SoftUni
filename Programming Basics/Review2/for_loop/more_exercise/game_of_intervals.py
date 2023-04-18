moves = int(input())
result = 0
first_group = 0
second_group = 0
third_group = 0
forth_group = 0
fifth_group = 0
invalid_group = 0
for _ in range(moves):
    current_number = int(input())
    if current_number > 50:
        result /= 2
        invalid_group += 1
    elif current_number < 0:
        result /= 2
        invalid_group += 1
    elif 0 <= current_number <= 9:
        result += current_number*0.2
        first_group += 1
    elif 10 <= current_number <= 19:
        result += current_number * 0.3
        second_group += 1
    elif 20 <= current_number <= 29:
        result += current_number * 0.4
        third_group += 1
    elif 30 <= current_number <= 39:
        result += 50
        forth_group += 1
    elif 40 <= current_number <= 50:
        result += 100
        fifth_group += 1
print(f"{result:.2f}")
print(f"From 0 to 9: {first_group/moves*100:.2f}%")
print(f"From 10 to 19: {second_group/moves*100:.2f}%")
print(f"From 20 to 29: {third_group/moves*100:.2f}%")
print(f"From 30 to 39: {forth_group/moves*100:.2f}%")
print(f"From 40 to 50: {fifth_group/moves*100:.2f}%")
print(f"Invalid numbers: {invalid_group / moves * 100:.2f}%")
