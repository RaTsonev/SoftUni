favorite_book = input()
checked_books = 0
while True:
    command = input()
    if command == favorite_book:
        print(f"You checked {checked_books} books and found it.")
        break
    if command == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {checked_books} books.")
        break
    checked_books += 1