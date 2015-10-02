# Jonathan Loescher SPC ID: 2307132

# Psuedocode
# Import temps module.
# Define main function.
# Define variable fahrenheit and ask user for input and convert input to a float value, then assign to the variable fahrenheit.
# Define variable cel_convert then execute fahr_to_celsius function in temps module and pass fahrenheit value. Then assigne return to cel_convert variable.
# Print value of cel_convert variable accurate to two decimal places with user friendly verbiage.
# Define variable celsius and ask user for input and convert input to a float value, then assign to the variable celsius.
# Define variable fahr_convert then execute celsius_to_fahr function in temps module and pass celsius value. Then assign the return to fahr_convert variable.
# Print value of fahr_convert variable accurate to two decimal places with user friendly verbiage.

import temps  # Import temps module.

def main():  # Define main function.
    fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))
    cel_convert = temps.fahr_to_celsius(fahrenheit)  # Execute fahr_to_celsius function in temps module and pass fahrenheit value. Then assigne return to cel_convert variable.
    print("In Celsius, that's ", format(cel_convert, '.2f'), " degrees.", sep='')  #

    celsius = float(input("Enter the temperature in degrees Celsius: "))
    fahr_convert = temps.celsius_to_fahr(celsius)  # Execute celsius_to_fahr function in temps module and pass celsius value. Then assign the return to fahr_convert variable.
    print("In Fahrenheit, that's ", format(fahr_convert, '.2f'), " degrees.", sep='')

# Collaboration Statement: I worked alone.
