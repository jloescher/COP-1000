#### list_file_read3.py
#### list elements are read back from a file

def main():
    # open file for reading
    myfile = open('friends.txt','r')

    names_list = []

    # use a for loop to process file
    for line in myfile:
        # strip the \n from each line and append onto list
        names_list.append(line.rstrip('\n'))
        # attempt read of another line

    myfile.close()
    print('These are my friends:')
    print(names_list)

    
main()



