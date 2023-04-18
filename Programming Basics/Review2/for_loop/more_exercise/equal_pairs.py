pairs = int(input())
first_pair = int(input()) + int(input())
diff = 0
for _ in range(1,pairs):
    current_pair = int(input()) + int(input())
    if current_pair != first_pair:
        if diff < abs(current_pair-first_pair):
            diff = abs(current_pair - first_pair)
    first_pair = current_pair
if diff == 0:
    print(f"Yes, value={first_pair}")
else:
    print(f"No, maxdiff={diff}")

