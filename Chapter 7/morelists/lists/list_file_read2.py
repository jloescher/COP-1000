#### list_file_read2.py
#### list elements are read back from a file

def main():
    # open file for reading
    myfile = open('friends.txt','r')

    names_list = []

    line = myfile.readline()  # this is the "priming read"

    # use a while loop to process file
    while line != '':
        # strip the \n from each line and append onto list
        names_list.append(line.rstrip('\n'))
        # attempt read of another line
        line = myfile.readline()

    myfile.close()
    print('These are my friends:')
    print(names_list)

    
main()



