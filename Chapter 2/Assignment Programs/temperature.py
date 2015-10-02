# Jonathan Loescher SPC ID: 2307132

# Formula: T(°F) = T(°C) × 1.8 + 32

# Pseudocode
# Prompt user to enter the temperature in Celsius.
# Multiply the value entered by the user (variable) by a float of 1.8 and add an integer of 32 and create a variable called "fahrenheit" to hold the sum.
# Display the results of the calculation (from fahrenheit variable) in a user friendly format.

def main():
    celsius = int(input('What is the temperature in Celsius? ')) # Asking user to input the temperature in Celsius
    fahrenheit = celsius * 1.8 + 32 # Using formula to convert Celsius to Fahrenheit
    # Displaying result of the calculations in a user friendly format.
    print("The Fahrenheit temperature is: ", format(fahrenheit, '.1f'), "°F", sep='') # Degree symbol is alt+248
    # Included sep='' to eliminate seperation between concatination.

main()

# Colaboration Statement:
# I used the below website to locate the formula for the program.
# http://www.rapidtables.com/convert/temperature/how-celsius-to-fahrenheit.htm
# I used the below website for reference of the degree symbol's ascii code.
# http://www.theasciicode.com.ar/extended-ascii-code/degree-symbol-ascii-code-248.html
# All work done by me except for the reference of the formula and ascii code.
