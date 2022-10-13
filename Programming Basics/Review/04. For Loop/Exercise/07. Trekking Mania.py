groups = int(input())
people = 0
musala_people = 0
monblan_people = 0
kilimanjaro_people = 0
k2_people = 0
everest_people = 0
for i in range(1, groups + 1):
    current_group = int(input())
    people += current_group
    if current_group <= 5:
        musala_people += current_group
    elif 6 <= current_group <= 12:
        monblan_people += current_group
    elif 13 <= current_group <= 25:
        kilimanjaro_people += current_group
    elif 26 <= current_group <= 40:
        k2_people += current_group
    elif 41 <= current_group:
        everest_people += current_group
musala_percentage = musala_people/people*100
monblan_percentage = monblan_people/people*100
kilimanjaro_percentage = kilimanjaro_people/people*100
k2_percentage = k2_people/people*100
everest_percentage = everest_people/people*100
print(f"{musala_percentage:.2f}%")
print(f"{monblan_percentage:.2f}%")
print(f"{kilimanjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")
