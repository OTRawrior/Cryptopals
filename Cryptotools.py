#! python 3
# Created by OTRawrior
# Function: Module containing crypto-related tools based on Cryptopals.

# Modules
from pprint import pprint

# Constants
BIN = '0000000100100011010001010110011110001001101010111100110111101111'
HEX = '0123456789ABCDEF'
B64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

HEX_BIN = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
           '4': '0100', '5': '0101', '6': '0110', '7': '0111',
           '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
           'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

B64_BIN = {'A': '000000', 'B': '000001', 'C': '000010', 'D': '000011',
           'E': '000100', 'F': '000101', 'G': '000110', 'H': '000111',
           'I': '001000', 'J': '001001', 'K': '001010', 'L': '001011',
           'M': '001100', 'N': '001101', 'O': '001110', 'P': '001111',
           'Q': '010000', 'R': '010001', 'S': '010010', 'T': '010011',
           'U': '010100', 'V': '010101', 'W': '010110', 'X': '010111',
           'Y': '011000', 'Z': '011001', 'a': '011010', 'b': '011011',
           'c': '011100', 'd': '011101', 'e': '011110', 'f': '011111',
           'g': '100000', 'h': '100001', 'i': '100010', 'j': '100011',
           'k': '100100', 'l': '100101', 'm': '100110', 'n': '100111',
           'o': '101000', 'p': '101001', 'q': '101010', 'r': '101011',
           's': '101100', 't': '101101', 'u': '101110', 'v': '101111',
           'w': '110000', 'x': '110001', 'y': '110010', 'z': '110011',
           '0': '110100', '1': '110101', '2': '110110', '3': '110111',
           '4': '111000', '5': '111001', '6': '111010', '7': '111011',
           '8': '111100', '9': '111101', '+': '111110', '/': '111111'}


class ClassName:
    def __init__(self):
        pass


# Functions
def convert_to_binary(value, conv_dict=HEX_BIN):
    """Convert a nonbinary value to binary.

    - value = a number in a base that corresponds to conv_dict
    - conv_dict = a dictionary in which the keys are the non-binary
                  base characters and values are binary equivalents

    Input a 'value' and a conversion dictionary. Returns the binary
    string equivalent of the given value.
    Uses HEX_BIN dictionary by default.
    Raises an error if a non-valid character is used anywhere in value.
    """

    result = ''
    try:
        for subvalue in value:
            result += conv_dict.get(subvalue)
        return result
    except TypeError:
        return 'Ensure input value characters are valid for the given base.'


def convert_from_binary(value, conv_dict=HEX_BIN):
    """Convert a binary string to a different base.

    - value = a number in binary
    - conv_dict = a dictionary in which the keys are the non-binary
                  base characters and values are binary equivalents

    Input a 'value' and a conversion dictionary. Returns the given base
    string equivalent of the given value.
    Uses HEX_BIN dictionary by default.
    Raises an error for non-valid characters or wrong number of bits.
    """

    result = ''
    slice_length = len(list(conv_dict.values())[0])  # Get length of first dict value
    i = 0
    try:
        while i < len(value):
            result += list(conv_dict.keys())[list(conv_dict.values()).index(value[i:i+slice_length])]
            i += slice_length
        return result
    except ValueError:
        return 'Ensure input values are binary of string length a multiple of the base.'


def convert_base_to_base(value, start_dict=HEX_BIN, end_dict=B64_BIN):
    """Convert a string to a different base.

    - value = a number in a base
    - start_dict = a dictionary in which the keys are the characters of
                   the starting base and values are binary equivalents
    - end_dict = a dictionary in which the keys are the characters of
                 the desired based and values are binary equivalents

    Input a 'value' and start/end dictionaries. Returns the given base
    in the new base.
    Uses HEX_BIN and B64_BIN as start/end dictionaries by default.
    """

    start = convert_to_binary(value, start_dict)
    return convert_from_binary(start, end_dict)


def main():
    return


if __name__ == '__main__':
    main()
