nylon = int(input()) + 2
paint = int(input())
thinner = int(input())
hours = int(input())

sum_nylon = nylon*1.5
sum_paint = (paint + paint*0.1)*14.5
sum_thinner = thinner*5
workers_per_hour = (sum_thinner + sum_paint + sum_nylon + 0.40)*0.3

final_sum = sum_thinner + sum_paint + sum_nylon + 0.40 + hours*workers_per_hour
print(final_sum)