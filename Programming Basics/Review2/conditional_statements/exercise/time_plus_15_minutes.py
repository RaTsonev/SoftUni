hours = int(input())
minutes = int(input())
time_in_minutes = hours*60 + minutes
added_time = time_in_minutes + 15

new_hours = added_time//60
new_minutes = added_time % 60

if new_hours > 23:
    if new_minutes >= 10:
        print(f"0:{new_minutes}")
    elif new_minutes == 0:
        print(f"0:00")
    else:
        print(f"0:0{new_minutes}")
else:
    if new_minutes >= 10:
        print(f"{new_hours}:{new_minutes}")
    else:
        print(f"{new_hours}:0{new_minutes}")