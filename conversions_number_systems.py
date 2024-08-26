import math
"""
Basic conversion between binary systems. All number systems stored as strings, to go through programatic logic of conversion. 
Suffix represents the base. 

Binary = "1010101_2"
Decimal = "75_10"
Octal = "11_8"
Hexadecimal = "7B316_16"

"""

BASE_10  = "_10"
BASE_2 = "_2"

# returns the number without suffix
def strip_suffix(number):
    indx = number.index("_")
    return number[0:indx]

def binary_to_decimal(binary):
    binary = strip_suffix(binary)
    decimal_int = 0  # int
    exponent = 0
    for i in range(len(binary)-1, -1, -1):  # iterate binary string from reverse, end to start
        binary_digit = int(binary[i])
        decimal_int += binary_digit * math.pow(2, exponent)
        # print(binary_digit, exponent)
        exponent += 1  # increment exponent

    decimal = str(int(decimal_int)) + BASE_10  # convert to int ot remove .0
    return decimal

def decimal_to_binary(decimal):
    decimal_num = int(strip_suffix(decimal))
    
    remainder_str = ""  # stores binary digits / remainders
    quotient = decimal_num  # initally set quotient to original decimal to be divided
    while quotient != 0:   # keep dividing until quotient is zero
        cur_remainder = quotient % 2        # remainder is the cur-quotient (what we just divided) modulo 2, compute remainder before quotient because qwhen we compute quotient it becomes new quotient for next division
        quotient = quotient // 2         # int division to get quotient, divide quotient of previous division
        remainder_str += str(cur_remainder) # add remainder which is binary digit to string
        # print(quotient, cur_remainder)
    remainder_str = remainder_str[::-1] # reverse binary digits
    return remainder_str + BASE_2


def main():

    print("Convert binary to decimal")
    binary = "10101010101011" + BASE_2
    decimal = binary_to_decimal(binary)
    print(f"binary {binary} is decimal {decimal}")

    print("\nConvert decimal to binary")
    decimal = "1231" +  BASE_10
    binary = decimal_to_binary(decimal)
    print(f"decimal {decimal} is binary {binary}")

if __name__ == "__main__":
    main()