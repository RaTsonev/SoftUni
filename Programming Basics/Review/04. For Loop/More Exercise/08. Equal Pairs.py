pairs = int(input())
pair = int(input()) + int(input())
diff = 0
for n in range(1, pairs):
    next_pair = int(input()) + int(input())
    if pair != next_pair:
        if diff < abs(pair - next_pair):
            diff = abs(pair - next_pair)
    pair = next_pair
if diff == 0:
    print(f"Yes, value={pair}")
else:
    print(f"No, maxdiff={diff}")