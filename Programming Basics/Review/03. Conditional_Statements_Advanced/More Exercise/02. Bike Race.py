junior_cyclists = int(input())
senior_cyslists = int(input())
route = input()
cyclists = junior_cyclists + senior_cyslists
money = 0
if route == "trail":
    money = junior_cyclists * 5.5 + senior_cyslists * 7
elif route == "cross-country":
    if cyclists < 50:
        money = junior_cyclists * 8 + senior_cyslists * 9.5
    if cyclists >= 50:
        money = junior_cyclists * 8 + senior_cyslists * 9.5 - (junior_cyclists * 8 + senior_cyslists * 9.5) * 0.25
elif route == "downhill":
    money = junior_cyclists * 12.25 + senior_cyslists * 13.75
elif route == "road":
    money = junior_cyclists * 20 + senior_cyslists * 21.50

money -= money * 0.05
print(f"{money:.2f}")