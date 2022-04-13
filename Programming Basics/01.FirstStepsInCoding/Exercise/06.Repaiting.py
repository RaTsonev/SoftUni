amount_nylon = int(input())
paint = int(input())
thinner = int(input())
hours_work = int(input())

price_amount_nylon = (amount_nylon + int(2))*1.50
price_paint = (paint + paint*0.1)*14.50
price_thinner = thinner*5
price_materials = (price_paint + price_thinner + price_amount_nylon + 0.40)
salary_per_hour = price_materials*0.30
salary = hours_work*salary_per_hour
final_price = price_materials +salary
print(final_price)

