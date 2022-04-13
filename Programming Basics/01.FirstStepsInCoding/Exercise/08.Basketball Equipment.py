annual_fee = int(input())

basketball_sneekers =annual_fee - annual_fee*0.4
basketball_outfit = basketball_sneekers - basketball_sneekers*0.2
ball =basketball_outfit*0.25
accessories = ball*0.2
costs = basketball_sneekers + basketball_outfit +ball + accessories + annual_fee

print(costs)
