current_number = float(input())

while current_number > 100 or current_number < 1:
    current_number = float(input())
print(f"The number {current_number} is between 1 and 100")