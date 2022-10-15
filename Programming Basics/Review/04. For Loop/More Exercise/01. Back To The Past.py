money = float(input())
years = int(input())
ivan_years = 18
for year in range(1800, years + 1):
    if year % 2 == 0:
        money -= 12000
    else:
        money -= 12000 + 50 * ivan_years
    ivan_years += 1
if money >= 0:
    print(f"Yes! He will live a carefree life and will have {abs(money):.2f} dollars left.")
else:
    print(f"He will need {abs(money):.2f} dollars to survive.")
