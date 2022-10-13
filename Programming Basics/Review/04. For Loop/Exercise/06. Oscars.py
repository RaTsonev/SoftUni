name_student = input()
points_academy = float((input()))
teachers = int(input())
points_student = points_academy
for i in range(1, teachers + 1):
    name_teacher = input()
    points_teacher = float(input())
    points_student += len(name_teacher) * points_teacher / 2
    if points_student > 1250.50:
        break
diff = 1250.5 - points_student
if points_student > 1250.50:
    print(f"Congratulations, {name_student} got a nominee for leading role with {points_student:.1f}!")
else:
    print(f"Sorry, {name_student} you need {diff:.1f} more!")