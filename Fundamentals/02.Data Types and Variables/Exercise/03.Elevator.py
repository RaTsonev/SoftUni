number_people = int(input())
capacity_people = int(input())
courses = number_people // capacity_people
if number_people % capacity_people > 0:
    print(courses + 1)
else:
    print(courses)