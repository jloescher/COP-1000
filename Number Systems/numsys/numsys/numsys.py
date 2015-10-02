#### module numsys.py
# several functions for converting base 10 numbers to other bases.

# function dec_base_2to9 converts a base-10 number to any base 2-9
def dec_base_2to9(base, num):
        convert = []
        while num != 0:
            convert.append(num % base)
            num = num // base
        convert.reverse()
        return_num = ''  ### string will hold converted number
        for digit in convert:
            return_num += str(digit)
        return return_num


# function dec_to_hex converts a base-10 number up to 255 to hex
def dec_to_hex(number):
    num = number
    convert = []
    while num != 0:
        remain = num % 16
        if remain == 10:
            convert.append('A')
        elif remain == 11:
            convert.append('B')
        elif remain == 12:
            convert.append('C')
        elif remain == 13:
            convert.append('D')
        elif remain == 14:
            convert.append('E')
        elif remain == 15:
            convert.append('F')
        else:
            convert.append(remain)
        num = num // 16
    convert.reverse()
    if number > 15:
        hex = str(convert[0])+ str(convert[1])
        return hex
    else:
        return convert[0]

