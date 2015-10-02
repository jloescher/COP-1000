# Jonathan Loescher SPC ID: 2307132

# Psuedocode
# Import Pythons Random Module.
# Define the main function.
# Create for loop counter in main function to call the randfind function 10 times.
# Define the randfind function.
# Create num variable
# Use randrange function in random module to assign a number between 10 and 50 to num variable
# Print value of num variable on same line separating by spaces.
# Execute main function.

import random  # Import random module.

def main():
    for count in range(10):  # Loop for count of 10.
        randfind()  # Call randfind function.

def randfind():
    num = random.randrange(10, 50)  # Assign random number between 10 and 50 to variable num.
    print(num, end=' ')  # Print num variable on same line with space as separation.

main()  # Execute main function.

# Collaboration Statement: I worked alone.
