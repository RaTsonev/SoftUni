bottles = int(input())
command = input()
detergent = bottles*750
times = 0
dishes = 0
pots = 0
while command != "End":
    command = int(command)
    times += 1
    if times < 3:
        detergent -= command*5
        dishes += command
    else:
        detergent -= command*15
        pots += command
        times = 0
    if detergent < 0:
        print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
        break
    command = input()
    if command == "End":
        print("Detergent was enough!")
        print(f"{dishes} dishes and {pots} pots were washed.")
        print(f"Leftover detergent {detergent} ml.")
        break
