money_vacation = float(input())
money = float(input())
spend_counter = 0
days = 0
while True:
    command = input()
    sum_spend_or_save = float(input())
    days += 1
    if command == "spend":
        money -= sum_spend_or_save
        spend_counter +=1
        if money < 0:
            money = 0
    elif command == "save":
        money += sum_spend_or_save
        spend_counter = 0
    if spend_counter == 5:
        print("You can't save the money.")
        print(days)
        break
    if money_vacation <= money:
        print(f"You saved the money for {days} days.")
        break
