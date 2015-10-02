# Jonathan Loescher SPC ID: 2307132

# Pseudocode
# Ask user to input a integer greater than 50 and less than 100 and store as "num" variable.
# Test If the value of "num" variable is greater than 50 and less than 100.
# Result is equal to true, then.
# Test If the integer stored in "num" variable is even.
# Result true, display "That was an even number."
# Else display "That was an odd number."
# Else in the event the "num" variable failed the test of being greater than 50 or less than 100 display "Bad Input."

def main():

    num = int(input("Please enter a number greater than 50 and less than 100, and I will tell you if it is odd or even: "))

    if num > 50 and num < 100: # Tests if number entered is between 50 - 100.
        if num % 2 == 0: # Test if even.
            print("That was an even number.")
        else: # If the number tests as odd.
            print("That was an odd number.")
    else:
        print("Bad Input.") # Number is outside of 50 - 100

main()

# Colaboration Statement: I worked alone.