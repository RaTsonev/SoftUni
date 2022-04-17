import math
record_seconds = float(input())
distance_meters = float(input())
swim_meter = float(input())

own_swimming = distance_meters*swim_meter
water_resistance = (math.floor(distance_meters / 15)*12.5)
swimming = own_swimming + water_resistance
if record_seconds > swimming:
    print(f" Yes, he succeeded! The new world record is {swimming:.2f} seconds.")
else:
    final_time = abs(record_seconds-swimming)
    print(f"No, he failed! He was {final_time:.2f} seconds slower.")
