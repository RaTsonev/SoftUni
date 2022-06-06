k = int(input())
l = int(input())
m = int(input())
n = int(input())
counter = 0
has_ended = False

for first_num_first_digit in range(k, 9):
    for first_num_second_digit in range(9, l-1, -1):
        for second_num_first_digit in range(m, 9):
            for second_num_second_digit in range(9, n-1, -1):
                first_number = first_num_first_digit * 10 + first_num_second_digit
                second_number = second_num_first_digit * 10 + second_num_second_digit
                if first_num_first_digit % 2 == 0 and second_num_first_digit % 2 == 0 and first_num_second_digit % 2 != 0 and second_num_second_digit %2 != 0 and first_number != second_number:
                    print(f"{first_number} - {second_number}")
                    counter += 1
                else:
                    print("Cannot change the same player.")
                if counter >= 6:
                    has_ended = True
                    break





