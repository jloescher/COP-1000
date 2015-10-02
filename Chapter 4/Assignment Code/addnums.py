# Jonathan Loescher SPC ID: 2307132

# Psuedocode
# Declare variable entries and set to amount accepted by program, which we chose 8 entries.
# Declare total and set value to 0.
# Create a for loop 'counter' and set the range to 'entries' variable.
# Within for loop declare num variable and ask for user input "Enter a number or 0 to quit: ".
# Within for loop create if statement to check if num is equal to 0, if so break out of loop.
# Within for loop create else statement in the even the if statement is not 'True' continue to
# add the num variable and total together and reassign to total variable.
# Outside of for loop print "The total is: " and display the value of the total variable.

def main():
    entries = 8 # Total amount of entries accepted.
    total = 0 # Declare total variable and set to 0.

    for counter in range(entries): # Create for loop and set range to value of entries variable.
        num = int(input("Enter a number or 0 to quit: ")) # Declare num variable and request user input.
        if num == 0: # Using if statement to test if num (user input) is equal to 0.
            break # If user input is equal to zero break out of loop.
        else: # If the if statement is not resolved as 'True' run the below statement.
            total = num + total # Add total variable and num variable together and reassign sum to total variable.
    print("The total is: ", total) # Print sum in a user friendly manor.

main()
    
# Colaboration Statement: I worked alone.
