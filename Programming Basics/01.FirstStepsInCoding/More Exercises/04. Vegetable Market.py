price_kg_vegetables = float(input())
price_kg_fruits = float(input())
kg_vegetables = int(input())
kg_fruits= int(input())

income = price_kg_vegetables*kg_vegetables + price_kg_fruits*kg_fruits
income_euro = income/1.94
print(f"{income_euro:.2f}")