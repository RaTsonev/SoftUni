price_per_page = float(input())
price_per_cover = float(input())
discount = int(input())
salary = float(input())
price_group = int(input())

sum = 899*price_per_page + 2*price_per_cover
sum = sum - sum*discount/100
designer = salary + sum
group = designer - designer*price_group/100
print(f"Avtonom should pay {group:.2f} BGN.")