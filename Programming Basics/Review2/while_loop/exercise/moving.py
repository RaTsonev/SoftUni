width = int(input())
length = int(input())
height = int(input())
free_space = width*length*height
command = input()

while command != "Done":
    luggage = int(command)
    free_space -= luggage
    if free_space < 0:
        print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
        break
    else:
        command = input()
        if command == "Done":
            print(f"{free_space} Cubic meters left.")
            break