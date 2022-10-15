command = input()
sum = 0
while command != "NoMoreMoney":
    current_command = float(command)
    if current_command < 0:
        print("Invalid operation!")
        print(f"Total: {sum:.2f}")
        break
    sum += current_command
    print(f"Increase: {current_command:.2f}")
    command = input()
if command == "NoMoreMoney":
    print(f"Total: {sum:.2f}")