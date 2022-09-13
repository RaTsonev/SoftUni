num_pen = int(input())
num_markers = int(input())
litres = int(input())
discount_percentage = int(input())
sum = num_pen*5.80 + num_markers*7.20 + litres*1.20
final_sum = sum - sum*(discount_percentage/100)
print(final_sum)