import math
"""
Basic conversion between binary systems. All number systems stored as strings, to go through programatic logic of conversion. 
Suffix represents the base. 

Binary = "1010101_2", "1010.101_2"
Decimal = "75_10"
Octal = "11_8"
Hexadecimal = "7B316_16"

More conversions to come.
"""

BASE_10  = "_10"  # speeds up typing dont have to type quotations :)
BASE_2 = "_2"
BASE_8 = "_8"
BINARY_TO_OCTAL = {
    '0000': '0',
    '0001': '1',
    '0010': '2',
    '0011': '3',
    '0100': '4',
    '0101': '5',
    '0110': '6',
    '0111': '7',
    '1000': '10',
    '1001': '11',
    '1010': '12',
    '1011': '13',
    '1100': '14',
    '1101': '15',
    '1110': '16',
    '1111': '17'
}

# HELPER FUNCTIONS
# returns the number without suffix
def strip_suffix(number):
    if "_" in number:
        indx = number.index("_")
        return number[0:indx]
    else:
        return number
# returns the integer part of a decimal omitting floating part
def get_integer_part(number):
    indx = number.index(".")
    return number[0:indx]+BASE_10
# returns the floating part of a decimal omiting integer part, includs point-.
def get_floating_part(number):
    indx = number.index(".")
    return number[indx:]



# in reverse order sum the products of the binary digit and its 2 to the power of digits index
def binary_to_decimal(binary):
    binary = strip_suffix(binary)
    decimal_int = 0  # int
    exponent_indx = 0
    for i in range(len(binary)-1, -1, -1):  # iterate binary string from reverse, end to start
        binary_digit = int(binary[i])
        decimal_int += binary_digit * math.pow(2, exponent_indx)
        # print(binary_digit, exponent)
        exponent_indx += 1  # increment exponent

    decimal = str(int(decimal_int)) + BASE_10  # convert to int ot remove .0
    return decimal

#  input binary-string has to be length of multiple 3 doesn't handle case where it is not.
def binary_to_octal(binary):
    binary = strip_suffix(binary)
    groups_of_three = []
    i = len(binary)-1
    while i >= 0:
        three_group = ""
        if i-2 >= 0:
            three_group += (binary[i-2] + binary[i-1] + binary[i])
            i = i-3
        else:
            print(f"{i=}, {three_group=}")
            three_group += binary[0:i]
            print(f"{i=}, {three_group=}")
            groups_of_three.append(three_group)
            break

        groups_of_three.append(three_group)
    
    groups_of_three.reverse()
    for i, group in enumerate(groups_of_three):
        while len(groups_of_three[i]) < 4: # because keys in dict are length 4
            groups_of_three[i] =  groups_of_three[i][:0] + '0' + groups_of_three[i][0:] # insert zero at beginning of string
    print(groups_of_three)

    octal = ""
    for group in groups_of_three:
        octal += BINARY_TO_OCTAL[group]
    
    return octal+BASE_8

# keep divding decimal by 2 until quotient is zero, then compile/reverse remainders of divisions
def decimal_to_binary(decimal):
    if decimal == "0_10": return "0000"+BASE_2
    # print(f"FLAG:{decimal}")
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

# first convert ineger part to binary noramlly then keep multiplying the fraction part of decimal by 2 (only multiply the fraction part of teh fraction part) until the fraction part's fraction part is all zeros, then compile the integer parts of all the fraction parts.
def floating_point_decimal_to_binary(decimal, precision=20):  # precision to prevent infinte loop, gives approximation
    
    integer_part = get_integer_part(decimal)   # get integer part of floating-point representation
    integer_part_binary = decimal_to_binary(integer_part)  # convert only integer part to binary
    i = 0  # just a counter
    # print(f"Integer part binary: {integer_part_binary}")

    floating_part = float(strip_suffix(get_floating_part(decimal)))

    integer_digits_str = ""
    while (floating_part % 1) != 0 and i < precision:
        floating_part_representation = str(floating_part)+BASE_10 # get representation to pass into get floating/integer part


        # set new floating-part for next multiplication equal to, 2 times only floating-part of the cur-floating-part, not multiplying the integer part of the cur-floating-part iwth 3
        # print(f"Float: {floating_part} * 2 = ")
        floating_part = float(strip_suffix(get_floating_part(floating_part_representation))) * 2
        # print(f"{floating_part}")
        
        if i != 0:
            integer_digits_str += str(strip_suffix(get_integer_part(str(floating_part_representation))))
        i+=1

    # one more iteration to multiply the floating
    floating_part_representation = str(floating_part)+BASE_10 # get representation to pass into get floating/integer part
    floating_part = float(strip_suffix(get_floating_part(floating_part_representation))) * 2
    integer_digits_str += str(strip_suffix(get_integer_part(str(floating_part_representation))))


    # print(integer_digits_str + BASE_2)
    final_floating_part_binary = integer_digits_str + BASE_2
    final_integer = strip_suffix(integer_part_binary)
    # print(f"Final Integer part binary: {final_integer}")
    # print(f"Final Floating part binary: {final_floating_part_binary}")
    final_binary = final_integer + "." + final_floating_part_binary
    return final_binary

def main():
    # input to functions is the string repsentation I defined
    print("Convert binary to decimal")
    binary = "10101010101011" + BASE_2
    decimal = binary_to_decimal(binary)
    print(f"binary {binary} is decimal {decimal}")

    print("\nConvert decimal to binary")
    decimal = "1231" +  BASE_10
    binary = decimal_to_binary(decimal)
    print(f"decimal {decimal} is binary {binary}")

    print("\nConvert floating point decimal to binary")
    decimal = "12.34" +  BASE_10
    binary = floating_point_decimal_to_binary(decimal)
    print(f"floating decimal {decimal} is binary {binary}")

    print("Convert binary to octal")
    binary = "010110101" + BASE_2
    octal = binary_to_octal(binary)
    print(f"binary {binary} is octal {octal}")

if __name__ == "__main__":
    main()