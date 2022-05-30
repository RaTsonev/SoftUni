n1 = int(input())
n2 = int(input())

for number in range(n1,n2+1):
    number_string = str(number)
    odd_sum = 0
    even_sum = 0

    for index, digit in enumerate(number_string):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if even_sum == odd_sum:
        print(number, end=" ")