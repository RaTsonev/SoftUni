number1=int(input())
number2=int(input())
operator = input()
result = 0
evenodd = ""
if number2 == 0:
    print(f"Cannot divide {number1} by zero")
else:
    if operator == "+" or operator == "-" or operator == "*":
        if operator == "+":
            result = number1 + number2
        elif operator == "-":
            result = number1 - number2
        elif operator == "*":
            result = number1 * number2
        if result % 2 == 0:
            evenodd = "even"
        else:
            evenodd = "odd"
        print(f"{number1} {operator} {number2} = {result} - {evenodd}")

    elif operator == "/":
        result = number1 / number2
        print(f"{number1} / {number2} = {result:.2f}")
    elif operator == "%":
        result = number1 % number2
        print(f"{number1} % {number2} = {result}")
