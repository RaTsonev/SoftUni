fuel = input()
amount_of_fuel = float(input())
card = input()
tax = 0
if card == "Yes":
    if fuel == "Gasoline":
        tax = amount_of_fuel * 2.04
    elif fuel == "Diesel":
        tax = amount_of_fuel * 2.21
    elif fuel == "Gas":
        tax = amount_of_fuel * 0.85
elif card == "No":
    if fuel == "Gasoline":
        tax = amount_of_fuel * 2.22
    elif fuel == "Diesel":
        tax = amount_of_fuel * 2.33
    elif fuel == "Gas":
        tax = amount_of_fuel * 0.93

if 20 <= amount_of_fuel <= 25:
    tax -= tax * 0.08
elif amount_of_fuel > 25:
    tax -= tax * 0.1

print(f"{tax:.2f} lv.")
