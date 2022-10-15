steps = int(input())
points = 0
part1 = 0
part2 = 0
part3 = 0
part4 = 0
part5 = 0
part_invalid = 0
for qwe in range(1, steps + 1):
    current_points = int(input())
    if 0 <= current_points <= 9:
        points += current_points * 0.2
        part1 += 1
    elif 10 <= current_points <= 19:
        points += current_points * 0.3
        part2 += 1
    elif 20 <= current_points <= 29:
        points += current_points * 0.4
        part3 += 1
    elif 30 <= current_points <= 39:
        points += 50
        part4 += 1
    elif 40 <= current_points <= 50:
        points += 100
        part5 += 1
    else:
        points = points / 2
        part_invalid += 1
group1 = part1 / steps * 100
group2 = part2 / steps * 100
group3 = part3 / steps * 100
group4 = part4 / steps * 100
group5 = part5 / steps * 100
group_invalid = part_invalid / steps * 100
print(f"{points:.2f}")
print(f"From 0 to 9: {group1:.2f}%")
print(f"From 10 to 19: {group2:.2f}%")
print(f"From 20 to 29: {group3:.2f}%")
print(f"From 30 to 39: {group4:.2f}%")
print(f"From 40 to 50: {group5:.2f}%")
print(f"Invalid numbers: {group_invalid:.2f}%")