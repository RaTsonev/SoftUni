actor_name = input()
points = float(input())
n = int(input())

for _ in range(n):
    jury_name = input()
    jury_points = float(input())
    points += (len(jury_name)*jury_points)/2

    if points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break
if points < 1250.5:
    diff = abs(1250.5 - points)
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")