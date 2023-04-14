money = float(input())
year = int(input())
ivan_years = 18
for current_year in range(1800, year + 1):
    if current_year % 2 == 0:
        money-= 12000
    else:
        money -= 12000 + 50*ivan_years
    ivan_years += 1
if money >=0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    print(f"He will need {abs(money):.2f} dollars to survive.")