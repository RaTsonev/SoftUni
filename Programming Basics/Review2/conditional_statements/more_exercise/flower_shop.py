import math
magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactus = int(input())
gift = float(input())

bill = magnolias * 3.25 + hyacinths * 4 + roses * 3.5 + cactus * 8
tax = bill*0.05
money_earned = bill-tax

if money_earned >= gift:
    print(f"She is left with {math.floor(money_earned-gift)} leva.")
else:
    print(f"She will have to borrow {math.ceil(gift-money_earned)} leva.")