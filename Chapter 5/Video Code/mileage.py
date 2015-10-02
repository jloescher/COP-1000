##### gas_mileage.py
# Finds and prints gas mileage after a trip
# using a function. User enters gas used and
# mileage data when program runs.
######### Pseudocode ##########
# For main()
# prompt user for odometer reading before trip, and
# assign to variable start_miles.
# prompt user for odometer reading after trip, and
# assign to variable end_miles.
# prompt user to enter gas used on trip, assign to gallons.
# call find_mileage function, passing in start_miles,end_miles
# and gallons...IN THIS ORDER.
#
# For find_mileage()
# subtract starting miles from ending miles, assign to miles
# divide miles by gallons, assign to mileage
# print the mileage accurate to 2 places of decimal

def main():
    start_miles = int(input('Starting odometer reading? '))
    end_miles = int(input('Ending odometer reading? '))
    gallons = float(input('Gallons of gas used? '))
    find_mileage(start_miles,end_miles,gallons)

def find_mileage(miles1,miles2,gas_used):
    miles = miles2 - miles1
    mileage = miles / gas_used
    print('Trip miles per gallon:',format(mileage,'.2f'))

main()
