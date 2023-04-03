import math
film_name = input()
duration_episode = int(input())
break_duration = int(input())

eating = break_duration/8
chilling_out = break_duration/4
time_left = break_duration - eating - chilling_out

if time_left >= duration_episode:
    print(f"You have enough time to watch {film_name} and left with {math.ceil(time_left-duration_episode)} minutes free time.")
else:
    print(f"You don't have enough time to watch {film_name}, you need {math.ceil(duration_episode-time_left)} more minutes.")