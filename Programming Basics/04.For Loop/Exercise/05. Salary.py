tabs_count = int(input())
salary = int(input())
for i in range(1, tabs_count+1):
    kind_site = input()
    if kind_site == "Facebook":
        salary -= 150
    elif kind_site == "Instagram":
        salary -= 100
    elif kind_site == "Reddit":
        salary -= 50
    else:
        salary -= 0
    if salary <= 0:
        print("You have lost your salary.")
        break
if salary > 0:
    print(salary)


