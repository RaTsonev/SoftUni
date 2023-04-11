screening = input()
rows = int(input())
columns = int(input())
income = 0
if screening == "Premiere":
    income = rows * columns * 12
elif screening == "Normal":
    income = rows * columns * 7.50
elif screening == "Discount":
    income = rows * columns * 5
print(f"{income:.2f} leva")