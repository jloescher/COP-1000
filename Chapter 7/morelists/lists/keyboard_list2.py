#### keyboard_list2.py

WEEKLY_WORK_DAYS = 5

def main():
    # create a list for weekly sales
    sales = [0] * WEEKLY_WORK_DAYS
    
    # use a loop to enter weekly sales
    for day in range(WEEKLY_WORK_DAYS):
        print('Enter sales for day ',day + 1,': ',sep='',end='')
        sales[day] = float(input())

    # declare and initialize an accumulator
    total_sales = 0
    # use a 2nd loop to process sales list
    for day in range(WEEKLY_WORK_DAYS):
        total_sales += sales[day]

    # display sales "report"
    print('Total sales for week $',format(total_sales,',.2f'))
    avg_sales = total_sales / WEEKLY_WORK_DAYS
    print('Average daily sales $',format(avg_sales,',.2f'))

main()
        
