not_good_grades = int(input())

failed = 0
answered = 0
points = 0

last_problem = ""
average_score = 0


has_filed = True
while not_good_grades > failed:
    problem_name = input()
    grade = int(input())
    if problem_name == "Enough":
        has_filed = False
        break

    if grade <= 4:
        failed +=1
    points += grade
    answered += 1
    last_problem = problem_name


if has_filed:
    print(f"You need a break, {failed} poor grades.")
else:
    average_score = points/answered
    print(f"Average score: {average_score}")
    print(f"Number of problems: {answered}")
    print(f"Last problem: {last_problem}")


