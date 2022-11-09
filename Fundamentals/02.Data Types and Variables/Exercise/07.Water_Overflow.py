number_of_lines = int(input())
capacity = 255
water_counter = 0
for current_line in range(number_of_lines):
    liters = int(input())
    if capacity - liters < 0:
        print("Insufficient capacity!")
        continue
    capacity -= liters
    water_counter += liters