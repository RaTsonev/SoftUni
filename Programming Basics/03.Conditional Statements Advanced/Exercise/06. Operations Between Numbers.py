num1 = int(input())
num2 = int(input())
operator = input()

sum = 0
even_odd = ""
if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        sum = num1 + num2
    elif operator == "-":
        sum = num1 - num2
    elif operator == "*":
        sum = num1 * num2

    if sum % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{num1} {operator} {num2} = {sum} - {even_odd}")

elif operator == "/":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        sum = num1/num2
        print(f"{num1} / {num2} = {sum:.2f}")
elif operator == "%":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        sum = num1 % num2
        print(f"{num1} % {num2} = {sum}")