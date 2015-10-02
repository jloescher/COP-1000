#### binary.py

class Binary:
    def __init__(self,bit_str):
        self.__bit_str = bit_str
        self.__bits = []                # create an empty list named bits
        for bit in range(len(bit_str)): # read string chara by chara
            self.__bits.append(int(bit_str[bit]))  # store to bits as ints

    def bin_2_decimal(self):
        bin_copy = [] + self.__bits     # make a copy of the list
        bin_copy.reverse()              # reverse the list
        base_10 = 0                     # to add up powers of 2 for ON bits
        for digit in range(len(bin_copy)):
            if bin_copy[digit] == 1:    
                base_10 += 2**digit     # accumulate if bit is ON
        return base_10        

    def bin_2_hex(self):
        return hex(self.bin_2_decimal())

