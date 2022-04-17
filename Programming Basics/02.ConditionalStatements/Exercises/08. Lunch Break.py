import math
movie = str(input())
movie_time = int(input())
lunch_break = int(input())

eat_time = lunch_break/8
break_time =lunch_break/4
time_left = lunch_break - eat_time - break_time
if movie_time <= time_left:
    time = math.ceil(time_left - movie_time)
    print(f"You have enough time to watch {movie} and left with {time} minutes free time.")
else:
    time = math.ceil(movie_time - time_left)
    print(f"You don't have enough time to watch {movie}, you need {time} more minutes.")

