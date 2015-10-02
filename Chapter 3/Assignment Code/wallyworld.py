# Jonathan Loescher SPC ID: 2307132

# Pseudocode
# Declare variable "children" and set to float of 5.00.
# Declare variable "youths" and set to float of 12.00.
# Declare variable "adults" and set to float of 20.00.
# Ask user to enter their age and store as an integer in variable "age".
# If "age" is less than 11 display $5.00 as the Admission Price.
# Else If "age" is less than 19 display $12.00 as the Admission Price.
# Else "age" is greater than or equal to 19 display $20.00 as the Admission Price.

def main():

    children = float(5.00)
    youths = float(12.00)
    adults = float(20.00)

    age = int(input("Please enter your age: ")) # Request input from user as integer.

    if age < 11: # Test if age is less than 11.
        print("You're admission price is $", format(children, '.2f'), ".", sep='')
    elif age < 19: # Test if age is less than 19.
        print("You're admission price is $", format(youths, '.2f'), ".", sep='')
    else: # Display below if value of age is 19 or greater.
        print("You're admission price is $", format(adults, '.2f'), ".", sep='')

main()

# Collaboration Statement: I worked alone.