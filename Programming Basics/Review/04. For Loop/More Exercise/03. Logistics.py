freights = int(input())
van_freights = 0
truck_freights = 0
train_freights = 0
sum_freights = 0
for num in range(1, freights + 1):
    freight = int(input())
    if freight <= 3:
        van_freights += freight
    elif 4 <= freight <= 11:
        truck_freights += freight
    elif freight >= 12:
        train_freights += freight
    sum_freights += freight
van = van_freights * 200
truck = truck_freights * 175
train = train_freights * 120
average = (van+truck+train)/sum_freights
print(f"{average:.2f}")
print(f"{(van_freights/sum_freights)*100:.2f}%")
print(f"{truck_freights/sum_freights*100:.2f}%")
print(f"{train_freights/sum_freights*100:.2f}%")
