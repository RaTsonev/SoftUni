holidays = int(input())
working_days = 365 - holidays
play_holidays = holidays*127
play_working_days = working_days*63
playing = play_working_days + play_holidays
diff = abs(playing - 30000)
hours = diff // 60
minutes = diff - hours*60
if playing > 30000:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")