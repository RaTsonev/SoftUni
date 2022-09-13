import math
pages = int(input())
pages_per_hour = int(input())
days = int(input())
book_hours = math.floor(pages/pages_per_hour)
book_days = book_hours/days
print(book_days)