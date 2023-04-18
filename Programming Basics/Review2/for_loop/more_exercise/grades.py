students = int(input())
num = 0
top = 0
good = 0
third = 0
fail = 0
average = 0
grades_sum = 0
for _ in range(students):
    grade = float(input())
    grades_sum += grade
    num += 1
    if grade >= 5.00:
        top += 1
    elif 4 <= grade <= 4.99:
        good += 1
    elif 3 <= grade <= 3.99:
        third += 1
    elif grade < 3.00:
        fail += 1
failed_students = fail*100/num
average_grade = grades_sum/num
print(f"Top students: {top/num*100:.2f}%")
print(f"Between 4.00 and 4.99: {good/num*100:.2f}%")
print(f"Between 3.00 and 3.99: {third/num*100:.2f}%")
print(f"Fail: {failed_students:.2f}%")
print(f"Average: {average_grade:.2f}")
