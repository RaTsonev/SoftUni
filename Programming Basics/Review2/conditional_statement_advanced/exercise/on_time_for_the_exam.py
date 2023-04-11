exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

exam = exam_hour * 60 + exam_minute
arrive = arrive_hour * 60 + arrive_minute
later = arrive - exam
earlier = exam - arrive
if arrive > exam:
    print("Late")
elif 0 <= earlier <= 30:
    print("On time")
elif earlier > 30:
    print("Early")

if 0 < later < 60:
    print(f"{later} minutes after the start" )
elif earlier >= 60:
    hour = earlier // 60
    minute = earlier % 60
    if minute > 10:
        print(f"{hour}:{minute} hours before the start")
    else:
        print(f"{hour}:0{minute} hours before the start")
elif 0 < earlier < 60:
    print(f"{earlier} minutes before the start")
elif later >= 60:
    hour = later // 60
    minute = later % 60
    if minute > 10:
        print(f"{hour}:{minute} hours after the start")
    else:
        print(f"{hour}:0{minute} hours after the start")