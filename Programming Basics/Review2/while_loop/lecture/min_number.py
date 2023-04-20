import sys
min_number = sys.maxsize
command = input()
while command != "Stop":
    command = int(command)
    if command < min_number:
        min_number = command
    command = input()
print(min_number)