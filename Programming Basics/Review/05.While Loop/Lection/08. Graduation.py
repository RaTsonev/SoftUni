name_student = input()
year = 0
sum_grades = 0
fail = 0
average = 0
while True:
    grade = float(input())
    if 6.00 >= grade >= 4.00:
        year += 1
        sum_grades += grade
        average = sum_grades / year
    elif grade < 4:
        fail += 1
        if fail > 1:
            print(f"{name_student} has been excluded at {year} grade")
            break
        year += 1
    if year == 12:
        print(f"{name_student} graduated. Average grade: {average:.2f}")
        break
