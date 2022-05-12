import sys
num = int(input())
min_number = sys.maxsize
max_number = -sys.maxsize

for i in range(num):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    if current_number < min_number:
        min_number = current_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
