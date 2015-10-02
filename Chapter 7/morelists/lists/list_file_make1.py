#### list_file_make1.py
#### list elements are written to a file

def main():
    # create list of names
    names = ['Guido','Mary','Tom','Sarah','Tony']

    # open file for writing
    myfile = open('friends.txt','w')

    # use loop to write elements to file
    for element in names:
        myfile.write(element + '\n')

    myfile.close()   # close file
    print('File created successfully')

main()



