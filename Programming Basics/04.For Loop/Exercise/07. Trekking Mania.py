count_groups = int(input())
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
for i in range(1,count_groups+1):
    competitors = int(input())
    if competitors <= 5:
        musala += competitors
    elif 6 <= competitors <= 12:
        monblan += competitors
    elif 13 <= competitors <= 25:
        kilimanjaro += competitors
    elif 26 <= competitors <= 40:
        k2 += competitors
    elif competitors >= 41:
        everest += competitors
sum = musala + monblan + kilimanjaro + k2 + everest

competitors_musala = musala/sum*100
competitors_monblan = monblan/sum*100
competitors_kilimanjaro = kilimanjaro/sum*100
competitors_k2 = k2/sum*100
competitors_everest = everest/sum*100
print(f"{competitors_musala:.2f}%")
print(f"{competitors_monblan:.2f}%")
print(f"{competitors_kilimanjaro:.2f}%")
print(f"{competitors_k2:.2f}%")
print(f"{competitors_everest:.2f}%")