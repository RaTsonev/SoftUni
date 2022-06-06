paper = int(input())
cloth = int(input())
glue = float(input())
discount = int(input())

sum_paper = paper * 5.80
sum_cloth = cloth * 7.20
sum_glove = glue * 1.20

sum = sum_paper + sum_cloth + sum_glove
final_sum = sum - (sum * discount/100)
print(f"{final_sum:.3f}")