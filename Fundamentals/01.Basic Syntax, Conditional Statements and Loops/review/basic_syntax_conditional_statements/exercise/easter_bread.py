budget = float(input())
kg_flour = float(input())
eggs = kg_flour*0.75
milk = kg_flour * 1.25 / 4
bread_counter = 0
colored_eggs = 0
bread_price = kg_flour + eggs + milk
while budget >= bread_price:
    bread_counter += 1
    colored_eggs += 3
    if bread_counter % 3 == 0:
        colored_eggs -= bread_counter - 2
    budget -= bread_price
print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")