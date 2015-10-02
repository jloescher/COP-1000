# Jonathan Loescher SPC ID: 2307132

# Psuedocode
#
# Create main function.
# In the main function, declare the variable length and set to float, then ask the user for the length of the rectangle.
# In the main function, declare the variable width and set to float, then ask the user for the width of the rectangle.
# Create catch all assigning variables perimeter and area, then execute rectfind function and pass both variables length and width to the rectfind function.
# Print "Rectangle area is " and display area value with three decimal spaces and eliminate seperation.
# Print "Rectangle perimeter is " and display perimeter value with the decimal spaces and eliminate seperation.
# Create rectfind function.
# Declare the variable calPerimeter, then use equation (2 * (length + width)), assign result of equation to perimeter variable.
# Declare the variable calArea, then use equation (length * width), assign result of the equation to the perimeter variable.
# Execute main function.

def main():
    length = float(input('Enter the rectangle length: '))
    width = float(input('Enter the rectangle width: ')) 
    perimeter,area = rectfind(length, width)  # Execute rectfind function and pass length and width variables. while also assigning the return variables to perimeter and area.
    print('Rectangle area is ', format(area, '.3f'), sep='')  # Print area with 3 decimal places and no seperation between string and variable.
    print('Rectangle perimeter is ', format(perimeter, '.3f'), sep='')  # Print perimeter with 3 decimal places and no seperation between string and variable.

def rectfind(length, width):  # Does not have to have the same parameter name as variable passed, however it made sense for this program.
    calPerimeter = 2 * (length + width) # Solve perimeter.
    calArea = length * width  # Solve area.
    
    return calPerimeter, calArea  # Return variables perimeter and area to catch all statement.
        
main() # Execute main function.

# Collaboration Statement: I worked alone.
