import math
holiday = int(input())
working_day = 365 - holiday

play = holiday*127 + working_day*63
free_time = abs(30000 - play)
hours = math.floor(free_time // 60)
minutes = free_time - hours*60
if play >= 30000 :
    print("Tom will run away")
    print(f"{hours:} hours and {minutes:} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours:} hours and {minutes:} minutes less for play")


