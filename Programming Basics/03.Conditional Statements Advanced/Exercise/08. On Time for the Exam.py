
exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour*60 + exam_minutes
arrival_time = arrival_hour*60 + arrival_minutes
diff_time = abs(exam_time - arrival_time)

if arrival_time > exam_time:
    print("Late")
    if diff_time >= 60:
        hours = diff_time // 60
        minutes = diff_time % 60
        print(f"{hours}:{minutes:02d} hours after the start")
    else:
        print(f"{diff_time} minutes after the start")
elif arrival_time <= exam_time and diff_time <= 30:
    print("On time")
    if diff_time > 0:
        print(f"{diff_time} minutes before the start")
else:
    print("Early")
    if diff_time >= 60:
        hours = diff_time // 60
        minutes = diff_time % 60
        print(f"{hours}:{minutes:02d} hours before the start")
    else:
        print(f"{diff_time} minutes before the start")

