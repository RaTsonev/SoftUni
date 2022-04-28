volume = int(input())
pipe1 = int(input())
pipe2 = int(input())
hours = float(input())

final_pipe1 = pipe1*hours
final_pipe2 = pipe2*hours
pipes = final_pipe1 + final_pipe2
if volume >= pipes:
    filled = pipes/volume*100
    value_pipe1 = final_pipe1 / pipes*100
    value_pipe2 = final_pipe2 / pipes * 100
    print(f"The pool is {filled:.2f}% full. Pipe 1: {value_pipe1:.2f}%. Pipe 2: {value_pipe2:.2f}%.")
else:
    overflow = pipes - volume
    print(f"For {hours:.2f} hours the pool overflows with {overflow:.2f} liters.")