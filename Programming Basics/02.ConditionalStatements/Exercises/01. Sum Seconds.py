time1 = int(input())
time2 = int(input())
time3 = int(input())
sum_time = time1 +time2 +time3

minutes = sum_time // 60
seconds = sum_time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
