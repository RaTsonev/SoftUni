import math
pages = int(input())
pages_per_hour = int(input())
days_per_book = int(input())

hours_whole_book =  math.floor(pages/pages_per_hour)
needed_hours_per_day =hours_whole_book/days_per_book
print(needed_hours_per_day)