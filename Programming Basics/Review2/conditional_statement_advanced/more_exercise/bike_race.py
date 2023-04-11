juniors = int(input())
seniors = int(input())
route = input()
sum_juniors = 0
sum_seniors = 0
if route == "trail":
    sum_juniors = juniors*5.5
    sum_seniors = seniors*7
elif route == "cross-country":
    sum_juniors = juniors*8
    sum_seniors = seniors*9.5
elif route == "downhill":
    sum_juniors = juniors*12.25
    sum_seniors = seniors*13.75
elif route == "road":
    sum_juniors = juniors*20
    sum_seniors = seniors*21.5
sum = sum_juniors + sum_seniors
if juniors+seniors >= 50 and route=="cross-country":
    sum -= sum*0.25
sum -= sum*0.05
print(f"{sum:.2f}")

