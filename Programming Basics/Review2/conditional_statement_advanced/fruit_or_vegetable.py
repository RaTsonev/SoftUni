product = input()
fruit = ["banana", "apple" , "kiwi", "cherry", "lemon" , "grapes"]
vegetables = ["tomato", "cucumber", "pepper" , "carrot"]

if product in fruit:
    print("fruit")
elif product in vegetables:
    print("vegetable")
else:
    print("unknown")