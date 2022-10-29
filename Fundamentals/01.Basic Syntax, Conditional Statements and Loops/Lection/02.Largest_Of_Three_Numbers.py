import sys
number1 = int(input())
number2 = int(input())
number3 = int(input())
max_number = -sys.maxsize
if number1 > max_number:
    max_number = number1
if number2 > max_number:
    max_number = number2
if number3 > max_number:
    max_number = number3
print(max_number)