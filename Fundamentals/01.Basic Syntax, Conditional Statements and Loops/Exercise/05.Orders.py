number_of_orders = int(input())
price = 0
total_sum = 0
for _ in range(number_of_orders):
    price_per_capsule = float(input())
    day = int(input())
    capsules_per_day = int(input())
    if 0.01 <= price_per_capsule <= 100 and 1 <= day <= 31 and 1 <= capsules_per_day <= 2000:
        price = capsules_per_day * price_per_capsule * day
        print(f"The price for the coffee is: ${price:.2f}")
        total_sum += price
    else:
        continue
print(f"Total: ${total_sum:.2f}")