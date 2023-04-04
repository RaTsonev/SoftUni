kilometers = int(input())
travelling = input()
sum = 0
if kilometers < 20:
    if travelling == "day":
        sum = 0.7 + kilometers*0.79
    elif travelling == "night":
        sum = 0.7 + kilometers * 0.9
elif kilometers < 100:
    sum = kilometers * 0.09
else:
    sum = kilometers * 0.06
print(f"{sum:.2f}")