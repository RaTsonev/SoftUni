total_steps = 0
mission = False
while True:
    command = input()
    if command == "Going home":
        steps = int(input())
        total_steps += steps
        break
    steps = int(command)
    total_steps += steps
    if total_steps >= 10000:
        mission = True
        print("Goal reached! Good job!")
        print(f"{total_steps-10000} steps over the goal!")
        break
if command == "Going home":
    if total_steps > 10000:
        print("Goal reached! Good job!")
        print(f"{total_steps-10000} steps over the goal!")
    else:
        print(f"{10000-total_steps} more steps to reach goal.")