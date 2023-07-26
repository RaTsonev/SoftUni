quantity_decorations = int(input())
remaining_days = int(input())
ornament_set = 2
tree_skirts = 5
tree_garland = 3
tree_lights = 15
cost = 0
spirit = 0
for day in range(1,remaining_days+1):
    if day % 11 == 0:
        quantity_decorations += 2
    if day % 2 == 0:
        cost += ornament_set * quantity_decorations
        spirit += 5
    if day % 3 == 0:
        cost += (tree_skirts + tree_garland) * quantity_decorations
        spirit += 13
    if day % 5 == 0:
        cost += tree_lights * quantity_decorations
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        cost += tree_skirts + tree_garland + tree_lights
if remaining_days % 10 == 0:
    spirit -= 30
print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")