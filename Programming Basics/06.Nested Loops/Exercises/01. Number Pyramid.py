n = int(input())
counter = 1
is_pyramid = False
for row in range(1, n+1):
    for column in range(0, row):
        print(f"{counter}", end =" ")
        counter += 1

        if counter > n:
            is_pyramid = True
            break
    if is_pyramid:
        break
    print()