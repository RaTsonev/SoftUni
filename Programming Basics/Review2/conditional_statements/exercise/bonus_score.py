points = int(input())
bonus = 0
if points <= 100:
    bonus += 5
elif 100< points <1000:
    bonus += points * 0.2
else:
    bonus += points * 0.1

if points % 2 == 0:
    bonus += 1
elif points % 5 == 0:
    bonus += 2

print(bonus)
print(bonus+points)