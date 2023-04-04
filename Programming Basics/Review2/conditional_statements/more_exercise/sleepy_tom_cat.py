holidays = int(input())
working_days = 365-holidays

playing = holidays * 127 + working_days * 63
hours = abs(30000 - playing)//60
minutes = abs(30000 - playing)%60

if playing > 30000:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")