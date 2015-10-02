# Jonathan Loescher SPC ID: 2307132

# Months with less than 31 days
# Feburary, April, June, September, and November

# Pseudocode
# Assign string to append to the response for each month with less than 31 days.
# Ask user to enter one of the months that has less than 31 days and assign to variable "answer".
# Use if statement to test if the month selected has less than 31 days.
# If it is true display: "You're correct "month" does have XX days."
# If it is false display: "Sorry, "month" has 31 days."

def main():

    Febuary = "28 days except when it is a leap year there are 29 days"
    April = "30 days"
    June = "30 days"
    September = "30 days"
    November = "30 days"
        
    answer = input("Please enter a month name that has less than 31 days: ")
    
    if answer == "Febuary": # Tests is value of answer is "Febuary".
        print("You're correct! ", answer, " does have ", Febuary, ".", sep='')
    elif answer == "April": # Tests is value of answer is "April".
        print("You're correct! ", answer, " does have ", April, ".", sep='')
    elif answer == "June": # Tests is value of answer is "June".
        print("You're correct! ", answer, " does have ", June, ".", sep='')
    elif answer == "September": # Tests is value of answer is "September".
        print("You're correct! ", answer, " does have ", September, ".", sep='')
    elif answer == "November": # Tests is value of answer is "November"
        print("You're correct! ", answer, " does have ", November, ".", sep='')     
    else: # Diplays if none of the above test True.
        print("Sorry, ", answer, " has 31 days.", sep='')

main()

# Colaboration Statement: I worked alone.
