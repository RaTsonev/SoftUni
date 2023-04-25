bad = int(input())
bad_rating = 0
exercise = 0
average = 0
ratings = 0
last_problem = ""
while True:
    command = input()
    if command != "Enough":
        rating = int(input())
        if rating <= 4:
            bad_rating += 1
        ratings += rating
        exercise += 1
    else:
        average = ratings/exercise
        print(f"Average score: {average:.2f}")
        print(f"Number of problems: {exercise}")
        print(f"Last problem: {last_problem}")
        break
    if bad == bad_rating:
        print(f"You need a break, {bad_rating} poor grades.")
        break
    last_problem = command
