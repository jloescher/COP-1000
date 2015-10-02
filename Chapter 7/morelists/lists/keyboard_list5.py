#### keyboard_list5.py
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
    [total,average,high,low] = process_list(sales) ### catch returns in list
    
    # display sales "report"
    print('Total sales for week $',format(total,',.2f'))
    print('Average daily sales $',format(average,',.2f'))
    print('Weekly highest $',format(high,',.2f'))
    print('Weekly lowest $',format(low,',.2f'))    
    
def process_list(list_name): 
    # declare and initialize an accumulator
    total_sales = 0
    # assign highest and lowest to first element in list
    lo = list_name[0]
    hi = list_name[0]
    # use a 2nd loop to process sales list
    for day in range(WEEKLY_WORK_DAYS):
        total_sales += list_name[day]
        if list_name[day] > hi:
            hi = list_name[day]
        if list_name[day] < lo:
            lo = list_name[day]
    # compute average
    average = total_sales / WEEKLY_WORK_DAYS
    item_list = [total_sales,average,hi,lo]       
    # return the list
    return item_list


main()
        
