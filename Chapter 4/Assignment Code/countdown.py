# Jonathan Loescher SPC ID: 2307132

# Pseudocode.
# Declare count variable to a value of 10 for countdown.
# Create while loop that runs if count variable is greater or equal to 1.
# Within while loop print count variable and change default function of the print statement from newline to space.
# Within while loop subtract 1 from the count variable and reassign sum to count variable.
# Outside of while loop use print function to break to newline.
# Print "Lift Off!"

def main():
    count = 10 # Declare count variable at 10.
    while count >= 1: # Starts and continues while loop if count variable is greater or equal to 1.
        print(count, end=' ') # Prints count value and substitutes the default newline to a space.
        count = count - 1 # Subtracts 1 from the value of the count variable and reassigns it to the count variable.
    print() # Breaks to newline.
    print("Lift off!") # Prints "Lift Off!"

main()

# Colaboration Statement: I worked alone.
