# Jonathan Loescher SPC ID: 2307132

# Psuedocode
# Create main function.
# Create list of presidents Kennedy - Obama.
# Print string "Original list in main" for clarity.
# Create for loop to iterate through presidents list.
# Create new list using variable "president_slice" and slice items 2 - 7.
# Create new list using variable "president_playlist_sorted" assign it to function playlist and pass "president_slice"
# variable as argument.
# Declare variable index as 0.
# Print string "Back in main, list in reverse alpha order" for clarity.
# Create while loop to iterate through president_playlist_sorted list.
# In while loop use rstrip function to clean up president_playlist_sorted list.
# In while loop print each value of the president_playlist_sorted.
# In while loop increment index by 1 each time it runs till index is equal to length of list.
# Define playlist function.
# Print string "Not in main: list size is now " and display the list size of list "president_playlist" using
# len function.
# Create list with variable president_playlist_sorted and sort the list alphabetically in reverse order.
# Return president_playlist_sorted list to main function.

def main():

    presidents = ['Kennedy', 'Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Bush', 'Obama']

    print('Original list in main:')
    for surname in presidents:
        print(surname)

    president_slice = presidents[2:8]

    president_playlist_sorted = playlist(president_slice)  # Execute playlist and pass president_slice as an argument.

    index = 0
    print('Back in main, list in reverse alpha order:')
    while index < len(president_playlist_sorted):  # While index is less than the length of the list.
        president_playlist_sorted[index] = president_playlist_sorted[index].rstrip('\n')
        print(president_playlist_sorted[index])
        index += 1

def playlist(president_playlist):
    print('Not in main: list size is now ', len(president_playlist), sep='')
    president_playlist_sorted = sorted(president_playlist, reverse=True)  # Sort alphabetically and reverse.
    return president_playlist_sorted

main()

# Collaboration Statement: I worked alone.
