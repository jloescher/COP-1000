#### two_dim_list.py
#### a 2D list is a list of lists

def main():
    # create 2D list
    people = [['Tom','M',19],
              ['Sally','F',21],
              ['Jerry','M',20]]
    
    print('Sally is',people[1][2],'years of age')
    print(people[2][0],'is a',people[2][1])

    ### process with ONE loop
    for persons in range(len(people)):
        print(people[persons][0],', age',people[persons][2], \
              ', is a ',people[persons][1])

    ### process with NESTED loops    
    for row in range(0,3):
        for column in range(0,3):
            print(people[row][column],' ',end='')
        print()
    
main()



