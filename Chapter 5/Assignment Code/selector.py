# Jonathan Loescher SPC ID: 2307132

# Psuedocode
#
# Import randoms_sel, rectangle_sel, tempconvert_sel.
# Define selector function.
# Define count variable and set to numeric value of 1.
# Create while loop that runs as long as count is less than 10.
# Print user friendly data.
# Print selection menu.
# Ask user for input and convert number to string.
# Use if and elif and else statements to preform actions based on user menu selection.
# When user selection 1 through 3 selections call the main() function in the relevant module.
# When user selection is 4 notify the user that the program is terminating.
# When user selection is other than what is in the menu, ask for valid selection and re-prompt user.

import randoms_sel
import rectangle_sel
import tempconvert_sel

def selector():
    count = 1
    while count < 10:
        print("Hello, which assignment would you like to check? Please enter the relevant selection.")
        print("1. ", "randoms_sel.py")
        print("2. ", "rectangle_sel.py")
        print("3. ", "tempconvert_sel.py")
        print("4. ", "Exit")

        selection = input(str('Please, enter the numeric selection: '))

        if selection == "1":
            print()
            print('You have selected "randoms_sel.py", the programs output is below.')
            print()
            randoms_sel.main()
            print()
            print()

        elif selection == "2":
            print()
            print('You have selected "rectangle_sel.py", please follow the program instruction below.')
            print()
            rectangle_sel.main()
            print()
            print()

        elif selection == "3":
            print()
            print('You have selected "tempconvert_sel.py", please follow the program instruction below.')
            print()
            tempconvert_sel.main()
            print()
            print()

        elif selection == "4":
            print()
            print('Ending your session, have a nice day!')
            break

        else:
            print()
            print('Please enter a valid numeric selection.')
            print()

selector()
