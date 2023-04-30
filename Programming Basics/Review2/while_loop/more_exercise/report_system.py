money = int(input())
money_cash = 0
money_card = 0
paying = 1
people_cash = 0
people_card = 0
collected_money = money_cash + money_card
while True:
    command = input()
    if command == "End":
        print("Failed to collect required money for charity.")
        break
    command = int(command)
    if paying % 2 != 0:
        if command <= 100:
            money_cash += command
            people_cash += 1
            print("Product sold!")
        else:
            print("Error in transaction!")
    else:
        if command > 10:
            money_card += command
            people_card += 1
            print("Product sold!")
        else:
            print("Error in transaction!")
    paying += 1
    collected_money = money_cash + money_card
    if collected_money >= money:
        average_cash = money_cash / people_cash
        average_card = money_card / people_card
        print(f"Average CS: {average_cash:.2f}")
        print(f"Average CC: {average_card:.2f}")
        break
