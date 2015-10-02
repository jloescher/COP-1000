#### global.py
#### shows a global variable
#### and the global keyword

num = 10    # declares global variable

def main():
    print('In main, num is',num)
    #### next, we call the glob function
    glob()
    print('In main again, num is',num)

    

def glob():
    #### global num   # try with comment removed, too
    num = 12
    print('In glob, num is',num)
    



main()
