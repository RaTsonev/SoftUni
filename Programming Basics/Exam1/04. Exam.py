students = int(input())
grade = float()
sum_grade = 0
group1_counter = 0
group2_counter = 0
group3_counter = 0
group4_counter = 0
for i in range(0, students):
    current_grade = float(input())
    sum_grade += current_grade
    if current_grade < 3:
        group1_counter += 1
    elif 3 <= current_grade <= 3.99:
        group2_counter += 1
    elif 4 <= current_grade <= 4.99:
        group3_counter += 1
    elif current_grade >= 5:
        group4_counter += 1

group1 = (group1_counter/students)*100
group2 = (group2_counter/students)*100
group3 = (group3_counter/students)*100
group4 = (group4_counter/students)*100
average = sum_grade/students
print(f"Top students: {group4:.2f}%")
print(f"Between 4.00 and 4.99: {group3:.2f}%")
print(f"Between 3.00 and 3.99: {group2:.2f}%")
print(f"Fail: {group1:.2f}%")
print(f"Average: {average:.2f}")
