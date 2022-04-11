meters_for_landscaping = float(input())
price_for_landscaping = meters_for_landscaping*7.61
discount = price_for_landscaping*0.18
final_price = float(price_for_landscaping-discount)
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
