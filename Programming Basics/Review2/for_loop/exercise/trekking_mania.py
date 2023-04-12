groups = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
all = 0
for _ in range(groups):
    people = int(input())
    all += people
    if people <= 5:
        musala += people
    elif 6 <= people <= 12:
        monblan += people
    elif 13 <= people <= 25:
        kilimandjaro += people
    elif 26 <= people <= 40:
        k2 += people
    elif people >= 41:
        everest += people

print(f"{musala/all*100:.2f}%")
print(f"{monblan/all*100:.2f}%")
print(f"{kilimandjaro/all*100:.2f}%")
print(f"{k2/all*100:.2f}%")
print(f"{everest/all*100:.2f}%")