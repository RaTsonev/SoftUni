adults = 0
kids = 0
toys = 0
sweaters = 0
while True:
    command = input()
    if command.isnumeric():
        current_command = int(command)
        if current_command <= 16:
            kids += 1
            toys += 1
        elif current_command > 16:
            adults += 1
            sweaters += 1
    elif command == "Christmas":
        break

price_toys = toys * 5
price_sweaters = sweaters * 15
print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {price_toys}")
print(f"Money for sweaters: {price_sweaters}")



