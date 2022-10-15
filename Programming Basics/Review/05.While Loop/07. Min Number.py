import sys

command = input()
min_number = sys.maxsize
while command != "Stop":
    current_command = int(command)
    if current_command < min_number:
        min_number = current_command
    command = input()
print(min_number)