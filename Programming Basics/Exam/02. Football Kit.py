tshirt = float(input())
price = float(input())

shorts = tshirt * 0.75
socks = shorts * 0.2
boots = 2*(tshirt + shorts)

sum = tshirt + shorts + socks + boots
sum_discount = sum - (sum*0.15)
diff = abs(price - sum_discount)

if sum_discount >= price:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {sum_discount:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")