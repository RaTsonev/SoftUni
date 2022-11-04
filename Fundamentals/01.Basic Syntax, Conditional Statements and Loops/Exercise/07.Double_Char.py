command = ""
new_string = ""
while True:
    command = input()
    if command == "End":
        break
    if command == "SoftUni":
        continue
    for character in command:
        new_string += character * 2
    print(new_string)
    new_string = ""