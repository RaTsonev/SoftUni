import sys

max_number = -sys.maxsize
current_command = input()
while current_command != "Stop":
    command = int(current_command)
    if command > max_number:
        max_number = command
    current_command = input()
print(max_number)