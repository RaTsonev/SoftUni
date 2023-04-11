chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()
sum_chrysanthemums = 0
sum_roses = 0
sum_tulips = 0
flowers = chrysanthemums + roses + tulips
total = 0
if season == "Spring" or season == "Summer":
    sum_chrysanthemums = chrysanthemums * 2
    sum_roses = roses * 4.1
    sum_tulips = tulips * 2.5
elif season == "Autumn" or season == "Winter":
    sum_chrysanthemums = chrysanthemums * 3.75
    sum_roses = roses * 4.5
    sum_tulips = tulips * 4.15
cost_flowers = sum_roses + sum_chrysanthemums + sum_tulips
if holiday == "Y":
    cost_flowers += cost_flowers * 0.15
if tulips > 7 and season == "Spring":
    cost_flowers -= cost_flowers * 0.05
elif roses >= 10 and season == "Winter":
    cost_flowers -= cost_flowers * 0.1
if flowers >= 20:
    cost_flowers -= cost_flowers * 0.2
final_sum = cost_flowers + 2
print(f"{final_sum:.2f}")