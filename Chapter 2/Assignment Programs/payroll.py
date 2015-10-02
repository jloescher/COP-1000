# Jonathan Loescher SPC ID: 2307132

# Pseudocode
# Prompt the user for hours worked and store it in a variable of "hours" as a float.
# Prompt the user for the pay rate and store it in a variable of "payRate" as a float.
# Multiply "hours" by "payRate" and store sum as "grossPay".
# Display the "grossPay" result in a user friendly format.

def main():
    hours = float(input('Enter the hours worked: ')) # Accepting input from user, set as a float to acomodate for portions of an hour.
    payRate = float(input('Enter the hourly pay rate: ')) # Accepting input from user, set as a float to acomodate for cents.
    grossPay = hours * payRate # Multiplying both variables.
    # Displaying results in user friendly format.
    print ("The weekly gross pay is $", format(grossPay, ',.2f'), sep='')
    # Included format function to display comma and round to two decimal places.
    # Included sep='' to eliminate seperation between concatination.

main()

# Collaboration Statement: I worked alone.
