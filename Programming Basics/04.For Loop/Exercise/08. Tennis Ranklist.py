import math
tournaments = int(input())
points_ranking_list = int(input())
points = 0
win_counter = 0
for i in range(1 , tournaments+1):
    kind = input()
    if kind =="W":
        points += 2000
        win_counter +=1
    if kind =="F":
        points += 1200
    if kind =="SF":
        points += 720

final_points = points + points_ranking_list
average = math.floor(points/tournaments)
win = (win_counter/tournaments)*100
print(f"Final points: {final_points}")
print(f"Average points: {average}")
print(f"{win:.2f}%")
