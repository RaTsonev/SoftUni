amount_pen_packs = int(input())
amount_marker_packs = int(input())
litres_cleaning_spray= int(input())
discount= int(input())/100

price_pen = amount_pen_packs*5.80
price_markers = amount_marker_packs*7.20
price_litres = litres_cleaning_spray*1.20
bill = float(price_pen+price_markers+price_litres)
final_price = bill-(bill*discount)
print(final_price)
