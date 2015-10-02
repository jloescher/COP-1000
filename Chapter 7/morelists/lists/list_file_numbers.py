#### list_file_numbers.py
#### list of integer elements are written to a file

def main():
    # create list of integers from 10-100 by tens
    numbers = range(10,101,10)

    # open file for writing
    myfile = open('nums.txt','w')

    # use loop to write elements to file
    for element in numbers:
        ### NOTE ### convert number to string with str
        myfile.write(str(element) + '\n')

    myfile.close()   # close file
    print('File created successfully')

main()



