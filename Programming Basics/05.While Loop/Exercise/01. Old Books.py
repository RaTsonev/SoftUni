favorite_book = input()
book_counter = 0
current_book = input()
is_found = False

while current_book != "No More Books":
    if current_book == favorite_book:
        is_found = True
        break
    else:
        book_counter += 1
    current_book = input()
if is_found:
    print(f"You checked {book_counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_counter} books.")