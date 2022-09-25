number = int(input())
bonus1 = 0
bonus2 = 0

if number > 1000:
    bonus1 = number*0.1
elif number > 100:
    bonus1 = number*0.2
elif number <= 100:
    bonus1 += 5

if number % 2 == 0:
    bonus2 += 1
elif number % 10 == 5:
    bonus2 += 2
bonus = bonus1 + bonus2
final_points = bonus + number

print(bonus)
print(final_points)
