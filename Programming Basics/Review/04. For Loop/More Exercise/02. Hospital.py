period = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0
for days in range(1, period + 1):
    patients = int(input())
    if days % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    if patients <= doctors:
        treated_patients += patients
    else:
        diff = abs(patients-doctors)
        treated_patients += patients-diff
        untreated_patients += diff
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")