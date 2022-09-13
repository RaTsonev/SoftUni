length = int(input())
wide  = int(input())
height  = int(input())
other = float(input())

volume = length * wide * height *0.001
litres = volume*(1-other/100)
print(litres)
