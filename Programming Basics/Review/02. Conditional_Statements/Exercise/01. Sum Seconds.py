time1 = int(input())
time2 = int(input())
time3 = int(input())
time = time1 + time2 + time3
minutes = time//60
seconds = time%60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")