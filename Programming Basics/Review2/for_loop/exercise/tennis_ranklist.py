import math
tournaments = int(input())
points_in_ranklist = int(input())
points = 0
wins = 0
for _ in range(tournaments):
    stage = input()
    if stage == "W":
        points += 2000
        wins += 1
    elif stage == "F":
        points += 1200
    elif stage == "SF":
        points += 720
final_points = points_in_ranklist + points
average_points = points/tournaments
percentage = wins/tournaments*100
print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percentage:.2f}%")

