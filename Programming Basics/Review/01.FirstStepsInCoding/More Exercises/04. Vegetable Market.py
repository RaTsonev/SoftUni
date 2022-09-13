price_kg_vegetables = float(input())
price_kg_fruits = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())

final_price = (price_kg_fruits*kg_fruits + price_kg_vegetables*kg_vegetables)/1.94
print(f"{final_price:.2f}")