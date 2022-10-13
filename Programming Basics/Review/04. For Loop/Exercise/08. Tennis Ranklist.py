import math

number_tournaments = int(input())
points = int(input())
won_points = 0
tournaments_won = 0
for i in range (1,number_tournaments+1):
    end_tournament = input()
    if end_tournament == "W":
        won_points += 2000
        tournaments_won +=1
    if end_tournament == "F":
        won_points += 1200
    if end_tournament == "SF":
        won_points += 720
average_points = math.floor(won_points/number_tournaments)
final_points = points + won_points
wins = tournaments_won/number_tournaments*100
print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{wins:.2f}%")
