fuel = input()
litres = float(input())
if fuel == "Diesel" or fuel == "Gasoline" or fuel == "Gas":
    fuel = fuel.lower()
    if litres >= 25:
        print(f"You have enough {fuel}.")
    else:
        print(f"Fill your tank with {fuel}!")
else:
    print("Invalid fuel!")