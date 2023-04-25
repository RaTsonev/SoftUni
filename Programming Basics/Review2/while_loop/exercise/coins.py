coins = 0
money = float(input())*100
hundreds = int(money%1000)
while hundreds != 0:
    if hundreds >= 200:
        hundreds = hundreds-200
        coins += 1
        continue
    if hundreds >= 100:
        hundreds = hundreds - 100
        coins += 1
        continue
    if hundreds >= 50:
        hundreds = hundreds-50
        coins += 1
        continue
    if hundreds >= 20:
        hundreds = hundreds - 20
        coins += 1
        continue
    if hundreds >= 10:
        hundreds = hundreds - 10
        coins += 1
        continue
    if hundreds >= 5:
        hundreds = hundreds - 5
        coins += 1
        continue
    if hundreds >= 2:
        hundreds = hundreds - 2
        coins += 1
        continue
    if hundreds >= 1:
        hundreds = hundreds - 1
        coins += 1
        continue
print(coins)



