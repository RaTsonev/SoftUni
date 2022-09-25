import math

film = input()
episode_duration = int(input())
break_duration = int(input())

time_eating = break_duration/8
time_rest = break_duration/4
time_left = break_duration - time_rest - time_eating
if time_left >= episode_duration:
    diff = math.ceil(time_left - episode_duration)
    print(f"You have enough time to watch {film} and left with {diff} minutes free time.")
else:
    diff = math.ceil(episode_duration - time_left)
    print(f"You don't have enough time to watch {film}, you need {diff} more minutes.")