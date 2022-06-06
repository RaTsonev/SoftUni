import sys

min_number = sys.maxsize
current_command = input()
while current_command != "Stop":
    command = int(current_command)
    if command < min_number:
        min_number = command
    current_command = input()
print(min_number)