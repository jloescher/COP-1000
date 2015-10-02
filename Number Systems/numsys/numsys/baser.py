# Numbers from 1 to 17 in various bases.
# Take a long look at the output to understand Number Systems.
# NOTE: allowable digits for any base b are from 0 to (b-1).
# Stretch output window horizontally to eliminate text wrapping.

import numsys # contains functions dec_base_2to9 and dec_to_hex

def main():
    print('Base:10 ',end='')
    for n in range(1,18):
        print(n,'\t',sep='',end='')
    print('\n')
    for base in range(2,10):
        print('Base:',base,'\t',sep='',end='')        
        for n in range(1,18):
            print(numsys.dec_base_2to9(base,n),'\t',end='')
        print()
    print('\nBase:16 ',end='')
    for n in range(1,18):
        print(numsys.dec_to_hex(n),'\t',sep='',end='')

            
main()
