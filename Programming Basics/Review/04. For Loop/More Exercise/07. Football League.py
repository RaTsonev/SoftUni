fans_limit = int(input())
fans = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0
for _ in range(1, fans + 1):
    current_fan = input()
    if current_fan == "A":
        sector_a += 1
    elif current_fan == "B":
        sector_b += 1
    elif current_fan == "V":
        sector_v += 1
    elif current_fan == "G":
        sector_g += 1
fans_sector_a = sector_a / fans * 100
fans_sector_b = sector_b / fans * 100
fans_sector_v = sector_v / fans * 100
fans_sector_g = sector_g / fans * 100
fans_stadium = fans / fans_limit * 100

print(f"{fans_sector_a:.2f}%")
print(f"{fans_sector_b:.2f}%")
print(f"{fans_sector_v:.2f}%")
print(f"{fans_sector_g:.2f}%")
print(f"{fans_stadium:.2f}%")
