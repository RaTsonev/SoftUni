hour = int(input())
day = input()
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

if day in days and hour in range(10,19):
    print("open")
else:
    print("closed")