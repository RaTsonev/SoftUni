record_seconds = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())

time = distance_meters*seconds_per_meter
slow = (distance_meters//15) * 12.5
final_time = time + slow
diff = abs(record_seconds-final_time)
if final_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {final_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")