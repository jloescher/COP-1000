# Jonathan Loescher SPC ID: 2307132

# Psuedocode
# Define Main Function.
# Create variable myfile, then open filename "mynumbers.txt" in read mode.
# Create list with variable num.
# Create a for statement which reads each line of the file and appends it to the list variable num as an integer.
# Create a for statement which reads the values of the list num and prints them to the console.
# Create variable with name largest_num and use the python max function to find which entry of num list is the...
# ... largest and assign it to the variable largest_num.
# Print the largest_num variable to the console with user friendly verbiage.
# Close file.
# Execute Main Function.

def main():
    myfile = open('mynumbers.txt', 'r')  # Open file in read mode.

    num = []  # Create list with variable of num.

    for line in myfile:
        num.append(int(line.rstrip()))  # Read each line from the text file and convert to integer while storing in list (num).

    for integer in num:
        print(integer)  # Print values of list.

    largest_num = max(num)  # Get max integer and assign to variable largest_num.

    print('The largest number is: ', largest_num, end='', sep='')

    myfile.close()  # Close file.

main()

# Collaboration Statement: I worked alone.
