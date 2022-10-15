students = int(input())
first_group = 0
second_group = 0
third_group = 0
fourth_group = 0
result = 0
for person in range(1, students + 1):
    grade = float(input())
    if grade >= 5.00:
        first_group += 1
        result += grade
    elif 4.99 >= grade >= 4.00:
        second_group += 1
        result += grade
    elif 3.99 >= grade >= 3.00:
        third_group += 1
        result += grade
    else:
        fourth_group += 1
        result += grade
sum_groups = first_group + second_group + third_group + fourth_group
percentage_first_group = first_group/sum_groups*100
percentage_second_group = second_group/sum_groups*100
percentage_third_group = third_group/sum_groups*100
percentage_fourth_group = fourth_group/sum_groups*100
average = (result / sum_groups)

print(f"Top students: {percentage_first_group:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_second_group:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_third_group:.2f}%")
print(f"Fail: {percentage_fourth_group:.2f}%")
print(f"Average: {average:.2f}")