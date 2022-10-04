import math

hour_exam = int(input())
minutes_exam = int(input())
arrived_hour = int(input())
arrived_minutes = int(input())

exam_time = hour_exam * 60 + minutes_exam
arrival_time = arrived_hour * 60 + arrived_minutes
diff = exam_time - arrival_time

if diff >= 0:
    if diff <= 30:
        print("On time")
    elif diff > 30:
        print("Early")

if 0 < diff < 60:
    print(f"{diff} minutes before the start")
    diff_hours = diff // 60
    diff_minutes = diff % 60
if diff >= 60:
    diff_hours = diff // 60
    diff_minutes = diff % 60
    if diff_minutes < 10:
        print(f"{diff_hours}:0{diff_minutes} hours before the start")
    else:
        print(f"{diff_hours}:{diff_minutes} hours before the start")

if arrival_time > exam_time:
    print("Late")
    diff = abs(diff)
    diff_hours = diff // 60
    diff_minutes = diff % 60
    if diff < 60:
        print(f"{diff} minutes after the start")
    if diff >= 60:
        if diff_minutes < 10:
            print(f"{diff_hours}:0{diff_minutes} hours after the start")
        else:
            print(f"{diff_hours}:{diff_minutes} hours after the start")
