username = input()
password = input()
while True:
    command = input()
    if command == password:
        print(f"Welcome {username}!")
        break
