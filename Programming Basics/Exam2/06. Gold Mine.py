locations = int(input())

while True:
    for i in range(1, locations+1):
        extraction_expected_per_day = float(input())
        days = int(input())
        sum_extraction = 0
        average = 0
        for j in range(1, days + 1):
            extraction = int(input())
            sum_extraction += extraction
        average = sum_extraction/days
        if average >= extraction_expected_per_day:
            print(f"Good job! Average gold per day: {average:.2f}.")
        else:
            diff = abs(extraction_expected_per_day - average)
            print(f"You need {diff:.2f} gold.")