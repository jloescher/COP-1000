### numbases.py
### Converts base-10 number to desired new base (from 2 to 10).

def main():

    numb = int(input('Enter base-10 number to convert from [max 63 to convert to binary] '))
    base = int(input('Enter base to convert to [2 to 10] '))
    num = numb

    dig5 = num // base ** 5
    num = num % base ** 5
    dig4 = num // base ** 4
    num = num % base ** 4
    dig3 = num // base ** 3
    num = num % base ** 3
    dig2 = num // base ** 2
    num = num % base ** 2
    dig1 = num // base ** 1

    dig0 = num % base ** 1
    
    print(numb,'base-10 in base',base,'is ',end='')
    print(dig5,dig4,dig3,dig2,dig1,dig0,'. NOTE:disregard any preceding zeroes',sep='')
    print('\nEXPLANATION: NOTE x means multiply and ^ indicates exponent')
    print(numb,' = ',dig5,'x',base,'^5 + ',sep='',end='')
    print(dig4,'x',base,'^4 + ',sep='',end='')
    print(dig3,'x',base,'^3 + ',sep='',end='')
    print(dig2,'x',base,'^2 + ',sep='',end='')
    print(dig1,'x',base,'^1 + ',sep='',end='')
    print(dig0,'x',base,'^0',sep='')    

    print(numb,' = ',dig5 * base ** 5, " + ",sep='',end='')
    print(dig4 * base ** 4, " + ",sep='',end='')
    print(dig3 * base ** 3, " + ",sep='',end='')
    print(dig2 * base ** 2, " + ",sep='',end='')
    print(dig1 * base ** 1, " + ",sep='',end='')
    print(dig0 * base ** 0)
    print(numb,'=',numb)
    

main()


    
            
