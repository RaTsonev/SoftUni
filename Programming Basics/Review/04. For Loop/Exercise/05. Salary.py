opened_tabs = int(input())
salary = int(input())
lost_money = 0
for tab in range(1, opened_tabs + 1):
    current_tab = input()
    if current_tab == "Facebook":
        lost_money += 150
    elif current_tab == "Instagram":
        lost_money += 100
    elif current_tab == "Reddit":
        lost_money += 50
    diff = abs(salary - lost_money)
    if diff <= 0:
        print(f"You have lost your salary.")
        break

if salary > lost_money:
    diff = abs(salary - lost_money)
    print(diff)