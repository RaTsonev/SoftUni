import sys
max_number = -sys.maxsize
command = input()
while command != "Stop":
    command = int(command)
    if command > max_number:
        max_number = command
    command = input()
print(max_number)