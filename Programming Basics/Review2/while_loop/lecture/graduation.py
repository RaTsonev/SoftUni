name = input()
year = 0
counter = 0
final_assessment = 0
while True:
    assessment = float(input())
    year += 1
    if assessment < 4:
        counter += 1
        if counter == 2:
            print(f"{name} has been excluded at {year} grade")
            break
        year -= 1
    else:
        final_assessment += assessment
    if year == 12:
        final_assessment = final_assessment/12
        print(f"{name} graduated. Average grade: {final_assessment:.2f}")
        break