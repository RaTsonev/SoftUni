budget = float(input())
price_per_kg_flour = float(input())
bread_counter = 0
colored_eggs = 0
one_pack_eggs = 0.75 * price_per_kg_flour
milk = (1.25 * price_per_kg_flour) / 4
bread = price_per_kg_flour + one_pack_eggs + milk

while budget >= bread:
    bread_counter += 1
    budget -= bread
    colored_eggs += 3
    if bread_counter % 3 == 0:
        colored_eggs -= bread_counter - 2
print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
