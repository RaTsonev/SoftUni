volume = int(input())
p1=int(input())
p2=int(input())
hours = float(input())

filled = (p1+p2)*hours
p1_filled = p1*hours/filled*100
p2_filled = p2*hours/filled*100
if filled > volume:
    print(f"For {hours} hours the pool overflows with {filled-volume:.2f} liters.")
else:
    print(f"The pool is {filled/volume*100:.2f}% full. Pipe 1: {p1_filled:.2f}%. Pipe 2: {p2_filled:.2f}%.")