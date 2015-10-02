### bases_table.py
### Displays values from 1 to 10 in bases 2 to 9

def main():
    print('Disregard preceding zeroes.')
    print('Stretch window horizontally to see all columns.')
    print('\t   1\t 2\t 3\t 4\t 5\t 6\t 7\t 8\t 9\t 10')
    for base in range(2,10):
        print('Base',base,'  ',end='')
        for num in range(1,11):
            dig3 = num // base ** 3
            num = num % base ** 3
            dig2 = num // base ** 2
            num = num % base ** 2
            dig1 = num // base ** 1
            dig0 = num % base ** 1
            print(dig3,dig2,dig1,dig0,sep='',end='')
            print('\t',end='')
        print()

main()


    
            
