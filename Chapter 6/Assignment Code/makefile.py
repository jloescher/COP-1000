# Jonathan Loescher SPC ID: 2307132

# Psuedocode
# Import Pythons Random Module.
# Define the main function.
# Open file mynumbers.txt in write mode and assign to variable myfile.
# Create num variable and assign a random integer between 5 and 13.
# Create for loop to count a range of (value of) num variable.
# In the for loop create a variable of random_num and assign it a value of a random number between 10 and 20.
# In the for loop write the random_num value as a string and create a new line.
# Close the file.
# Advise once the file has completed.
# Execute main function.

import random  # Import random module for python.

def main():
    myfile = open('mynumbers.txt', 'w')  # Open file.

    num = random.randint(5, 13)  # Create random number between 5 and 13 and assign to num variable.

    for count in range(num):  # Run code below for as many times as value of num variable.
        random_num = random.randrange(10, 20)  # Create random number between 10 and 20 and assign to variable random_num.
        myfile.write(str(random_num) + '\n')  # Write random_num value as string in text file and create a new line.

    myfile.close()  # Close file
    print('File Completed.')  # Display when file is completed.

main()

# Collaboration Statement: I worked alone.
