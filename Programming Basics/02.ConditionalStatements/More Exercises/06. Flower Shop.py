import math
magnolias_num = int(input())
hyacinth_num = int(input())
roses_num = int(input())
cacti_num = int(input())
gift_price = float(input())

sum_magnolias = magnolias_num*3.25
sum_hyacinth = hyacinth_num*4
sum_roses = roses_num*3.5
sum_cacti = cacti_num*8

sum = sum_magnolias + sum_hyacinth + sum_roses + sum_cacti
tax = sum*0.05
free = sum-tax

if free >= gift_price:
    more = math.floor(free-gift_price)
    print(f"She is left with {more} leva." )
else:
    more = math.ceil(abs(free - gift_price))
    print(f"She will have to borrow {more} leva." )