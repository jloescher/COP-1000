#### keyboard_list1.py

WEEKLY_WORK_DAYS = 5

def main():
    # create a list for weekly sales
    sales = [0] * WEEKLY_WORK_DAYS
    
    # use a loop to enter weekly sales
    for day in range(WEEKLY_WORK_DAYS):
        print('Enter sales for day ',day + 1,': ',sep='',end='')
        sales[day] = float(input())

    # display (crudely) the list
    print(sales)

main()
        
