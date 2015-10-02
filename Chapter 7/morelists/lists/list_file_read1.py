#### list_file_read1.py
#### list elements are read back from a file

def main():
    # open file for reading
    myfile = open('friends.txt','r')

    # read entire file into a list
    names_list = myfile.readlines()

    myfile.close()   # close file

    # use a while loop to process list
    index = 0

    print(names_list)
    
    print('These are my friends:')
    while index < len(names_list):
        # strip out the \n from each element
        names_list[index] = names_list[index].rstrip('\n')
        print(names_list[index])
        index += 1

main()



