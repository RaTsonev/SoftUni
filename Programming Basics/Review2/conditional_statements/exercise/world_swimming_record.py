import math
record = float(input())
distance_in_meters = float(input())
time_swam_one_meter = float(input())

times_delay = distance_in_meters // 15
final_time = distance_in_meters * time_swam_one_meter + times_delay * 12.5

if record > final_time:
    print(f" Yes, he succeeded! The new world record is {final_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {final_time-record:.2f} seconds slower.")