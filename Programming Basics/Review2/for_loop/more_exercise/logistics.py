number_freight = int(input())
whole_freights = 0
bus = 0
truck = 0
train = 0

for _ in range(number_freight):
    freight = int(input())
    whole_freights += freight
    if freight <= 3:
        bus += freight
    elif 4 <= freight <= 11:
        truck += freight
    elif freight >= 12:
        train += freight
average_per_ton = (bus*200 + truck*175 + train*120)/whole_freights
average_bus = bus/whole_freights*100
average_truck = truck/whole_freights*100
average_train = train/whole_freights*100

print(f"{average_per_ton:.2f}")
print(f"{average_bus:.2f}%")
print(f"{average_truck:.2f}%")
print(f"{average_train:.2f}%")