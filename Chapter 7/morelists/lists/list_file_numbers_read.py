#### list_file_numbers_read.py
#### list of integer elements are read from a file

def main():
    # create empty list
    numbers = []

    # open file for reading
    myfile = open('nums.txt','r')

    # use loop to read elements from file
    for line in myfile:
        # convert string to integer with int and append
        numbers.append(int(line))

    myfile.close()   # close file
    print('Here are the numbers:')
    print(numbers)

main()



