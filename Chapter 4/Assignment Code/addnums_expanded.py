# Jonathan Loescher SPC ID: 2307132

# Pseudocode
# Declare the total variable and set it equal to 0.
# Declare the num variable and ask user to enter a number or type 0 to quit.
# Create while loop that runs if num variable is not set to 0.
# Within the while loop add the total variable with the num variable and assign back to total variable.
# Within the while loop ask user to enter another number or enter 0 to request total.
# Outside of while loop create if statement to check if total is equal to 0.
# If total is equal to 0 print "No numbers to add."
# Else print "The total is: " and display total variable.

def main():
    total = 0 # Declare total variable and set to 0.
    num = int(input("Enter a number or 0 to quit: ")) # Request user input.
    while num != 0: # If num is not equal to zero enter loop.
        total = total + num # Add total + num variable together.
        num = int(input("Enter a number or 0 to total: ")) # Request user input.
    if total == 0: # If total is equal to 0 print the below statement.
        print("No numbers to add.")
    else: # If total is not equal to 0 then print below statement and display total variable.
        print("The total is: ", total)

main()

# Colaboration Statement: I worked alone.
