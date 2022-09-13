num_chicken_menu = int(input())
num_fish_menu = int(input())
num_veggie_menu = int(input())

sum_menu = num_fish_menu*12.40 + num_veggie_menu*8.15 + num_chicken_menu*10.35
dessert=sum_menu*0.2
final_sum = sum_menu+dessert+2.5
print(final_sum)