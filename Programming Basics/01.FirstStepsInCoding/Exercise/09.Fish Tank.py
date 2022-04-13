lenght_cm = int(input())
width_cm = int(input())
height_cm = int(input())
occupied_palace = int(input())/100

volume = lenght_cm * width_cm * height_cm
volume_litres = volume/1000
needed_litres = volume_litres - volume_litres*occupied_palace

print(needed_litres)
