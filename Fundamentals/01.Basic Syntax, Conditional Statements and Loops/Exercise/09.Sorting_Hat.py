name = input()
length = 0
while name != "Welcome!":
    if name == "Voldemort":
        break
    length = len(name)
    if length < 5:
        print(f"{name} goes to Gryffindor.")
    elif length == 5:
        print(f"{name} goes to Slytherin.")
    elif length == 6:
        print(f"{name} goes to Ravenclaw.")
    elif length > 6:
        print(f"{name} goes to Hufflepuff.")
    name = input()
if name == "Voldemort":
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")
