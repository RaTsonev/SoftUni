volume = int(input())
pipe1_debit = int(input())
pipe2_debit = int(input())
missed_hours = float(input())

filled1 = pipe1_debit*missed_hours
filled2 = pipe2_debit*missed_hours
filled = filled1 + filled2
overflow = abs(volume - filled)
percentage = filled/volume*100
pipe1_percetage = filled1/filled*100
pipe2_percetage = filled2/filled*100
if volume >= filled:
    print(f"The pool is {percentage:.2f}% full. Pipe 1: {pipe1_percetage:.2f}%. Pipe 2: {pipe2_percetage:.2f}%.")
else:
    print(f"For {missed_hours} hours the pool overflows with {overflow} liters.")