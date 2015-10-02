#### test_binary.py

import binary

BIN = 1
DEC = 2
HEX = 3
QUIT = 4

def main():
    pick = 0
    while pick != QUIT:
        print()
        show_menu()
        pick = process_menu()

def show_menu():
    print('   NUMBER SYSTEMS MENU')
    print('1) Enter binary number')
    print('2) Enter decimal number')
    print('3) Enter hexadecimal number')
    print('4) Quit this program')    

def process_menu():
    pick = int(input('   Make a selection: '))
    if pick == BIN:
        bin_do()
    elif pick == DEC:
        dec_do()
    elif pick == HEX:
        hex_do()
    elif pick == QUIT:
        print()
        print('Exiting the program...')
    else:
        print('Invalid input. Try again.')
    return pick

def bin_do():
    bin = input('Enter the bits ')
    my_bits = binary.Binary(bin)
    dec = my_bits.bin_2_decimal()
    print(bin,'=',dec,'in decimal.')
    print(bin,'is',format(dec,'X'),'in hexadecimal.') 

def dec_do():
    dec = int(input('Enter the decimal number '))
    print(dec,'is',format(dec,'b'),'in binary.')
    print(dec,'is',format(dec,'X'),'in hexadecimal.')    

def hex_do():
    hex_in = input('Enter the hexadecimal number ')
    dec = int(hex_in,16)    # hex string to decimal
    print(hex_in,'=',format(dec,'b'),'in binary.')
    print(hex_in,'=',dec,'in decimal.')

main()
