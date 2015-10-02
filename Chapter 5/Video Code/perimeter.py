##### perimeter.py
# Finds and prints perimeter of a rectangle
# using a function. User enters dimensions.
######### Pseudocode ##########
# For main()
# prompt user to enter length, assign to length
# prompt user to enter width, assign to width
# run show_perimeter function, passing in length and width
#
# For show_perimeter()
# calculate perimeter using formula, assign to perimeter
# print the perimeter


def main():
    length = int(input('Enter the length '))
    width = int(input('Enter the width '))
    show_perimeter(length,width)

def show_perimeter(l,w):
    perimeter = 2 * (l + w)
    print('The perimeter is',perimeter)


main()
