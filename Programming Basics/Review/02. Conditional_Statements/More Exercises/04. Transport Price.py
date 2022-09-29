kilometers = int(input())
word = input()

if word == "day" and kilometers < 20:
    price = 0.70 + 0.79 * kilometers
    print(f"{price:.2f}")
elif word == "night" and kilometers < 20:
    price = 0.70 + 0.90 * kilometers
    print(f"{price:.2f}")
elif 20 <= kilometers <= 99:
    price = kilometers*0.09
    print(f"{price:.2f}")
elif kilometers >= 100:
    price = kilometers*0.06
    print(f"{price:.2f}")