hour = int(input())
minutes = int(input())
minutes_after_add = minutes + 15
if minutes_after_add >= 60:
    hour += 1
    minutes = minutes_after_add - 60
else:
    minutes = minutes_after_add
if hour == 24:
    hour = 0
elif hour > 24:
    hour = hour-24
if minutes < 10:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")