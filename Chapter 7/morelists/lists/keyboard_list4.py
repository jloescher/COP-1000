#### keyboard_list4.py
#### demos passing list to a function
#### also demos returning a list from a function

WEEKLY_WORK_DAYS = 5

def main():
    # create a list for weekly sales
    sales = [0] * WEEKLY_WORK_DAYS
    
    # use a loop to enter weekly sales
    for day in range(WEEKLY_WORK_DAYS):
        print('Enter sales for day ',day + 1,': ',sep='',end='')
        sales[day] = float(input())

    # call the process_list function
    [total,average] = process_list(sales) ### catch returns in list
    
    # display sales "report"
    print('Total sales for week $',format(total,',.2f'))
    print('Average daily sales $',format(average,',.2f'))
    
def process_list(list_name): 
    # declare and initialize an accumulator
    total_sales = 0
    # use a 2nd loop to process sales list
    for day in range(WEEKLY_WORK_DAYS):
        #### NOTE #### in function the list is known as list_name
        total_sales += list_name[day]
    total = sum(list_name)
    # return a list of two elements    
    return [total,(total_sales / WEEKLY_WORK_DAYS)]


main()
        
