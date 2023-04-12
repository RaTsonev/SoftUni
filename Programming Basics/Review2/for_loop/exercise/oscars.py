import math
actor_name = input()
points_from_academy = float(input())
examiner = int(input())
points = 0
for i in range(1,examiner+1):
    name_examiner = input()
    points_examiner = float(input())
    if i == 1:
        current_points =points_from_academy + len(name_examiner)*points_examiner/2
    else:
        current_points = len(name_examiner) * points_examiner / 2
    points += current_points
    if points >= 1250.5:
        break

if points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5-points:.1f} more!")