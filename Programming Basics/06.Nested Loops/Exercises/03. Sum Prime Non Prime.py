from math import sqrt
from math import ceil
command = input()
prime_sum = 0
non_prime_sum = 0

while command != "stop":
    current_number = int(command)
    if current_number < 0:
        command = input()

    if current_number <= 0:
        non_prime_sum += current_number
    else:
        is_prime = True
        for div in range(2, ceil(sqrt(current_number)) + 1):
             if current_number % div == 0:
                is_prime = False
                break
             if is_prime:
                 prime_sum += current_number
             else:
                 non_prime_sum += current_number
    command = input()
print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")