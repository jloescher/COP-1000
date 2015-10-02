#### ticket.py

def main():

    ticket = [[12,32,44,1,18,51],
              [1,2,3,4,5,6],
              [50,40,30,20,10,1],
              [22,32,12,42,52,2],
              [3,13,23,33,43,52]
              ]

    for row in range(len(ticket)):
        for column in range(len(ticket[row])):
            print(ticket[row][column],end=' ')
        print()

main()
