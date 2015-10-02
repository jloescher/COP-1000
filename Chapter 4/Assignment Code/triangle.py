# Jonathan Loescher SPC ID: 2307132

# Pseudocode
# Create loop with 7 lines printed using range starting with 1 and ending with 8.
# Create nested loop 'col1' which iterates though 1 - 7 and subtracts 1 each time it runs.
# In nested loop 'col1' print spaces in a row equal to the amount of times the for statement runs.
# Create nested loop 'col2' which iterates though 1 - 1 and adds the value of 'row' each time it runs.
# In nested loop 'col2' print 'o' in a row equal to the amount of times the for statement runs.
# In main loop create print() to create a newline for the next row to be printed on.

def main():
    for row in range(1, 8): # Starts with 1 and counts through till 7.
        for col1 in range(1, 8 - row): # Starts with 1 and counts through till 7 and then subtracts value of 'row'.
            print(' ', end='')
        for col2 in range(1, 1 + row): # Starts with 1 and counts through till 1 and then add the value of "row".
            print('o', end='')
        print()

main()

# Colaboration Statement: I worked alone.
