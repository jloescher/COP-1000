## from_base10.py
## converts a base-10 integer to a new base (2-9) or 16.
## NOTE: in explanation, ^ denotes exponent, 1 * 2^3 means 1 * 2 cubed.
## NOTE also the decreasing powers of the base, down to zero.

import numsys,sys

def main():

    base_10 = int(input('Enter a base-10 number to convert (max 255) '))
    if base_10 > 255:
        print('Bad input. Maximum number to convert is 255.')
        sys.exit()
    
    base = int(input('Now enter the desired new base (2-9 or 16) '))

    if base <= 9 and base > 1:
        result = numsys.dec_base_2to9(base,base_10)
        ### explanation
        exp = len(result) - 1

        result_str = str(base_10)+' = '
        for n in result:
            result_str += str(n)+' * '+str(base)+'^'+str(exp)
            if exp > 0:
                result_str += ' + '
            exp -= 1
        print(result_str)
    elif base == 16:
        ### no explanation for hex
        result = numsys.dec_to_hex(base_10)
    else:
        print('Bad input. Base must be an integer from 2-9 or 16.')
        sys.exit()

    print(base_10,'is',result,'in base',base)


main()
