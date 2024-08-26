"""
Coding systems

Binary Coded Decimal [BCD] each digit in decimal number is represented by a 4-bt binary number. 
represented as string "00010000_BCD"

Gray Code [GC] only 1 bit changes between adjacent codes
represented as string ""1010101_GC"
"""
from conversions_number_systems import decimal_to_binary, strip_suffix, BASE_10, BASE_2

BCD = "BCD"
GC = "GC"

# if binary string is not 4 digits adds zeros to prefix, pass in withou suffix
def get_4_bits(binary):
    while len(binary) < 4:
        binary = "0" + binary
    return binary
def XOR(d1, d2): # d1="1"
    if d1 == d2:
        return "0"
    if d1 != d2:
        return "1"


def decimal_to_BCD(decimal):
    decimal_striped = strip_suffix(decimal)
    bcd_str = ""
    for digit in decimal_striped:
        digit_representation = (digit + BASE_10)

        # print("Digit")
        # print(digit_representation, decimal_to_binary(digit_representation))

        # convert singular digit to binary
        digit_binary_code = strip_suffix(decimal_to_binary(digit_representation))
        digit_binary_4_bits = get_4_bits(digit_binary_code)
        bcd_str += digit_binary_4_bits
    
    return bcd_str + "_"+BCD

def binary_to_gray_code(binary):
    binary = strip_suffix(binary) 
    print(binary)
    gray_code = binary[0]  # drop down first bit

    for i in range(len(binary)):
        if i+1 <= len(binary)-1:
            bit1, bit2 = binary[i], binary[i+1]  # takes adjacent pairs of binary bits as input into XOR
            gray_code_bit = XOR(bit1, bit2)
            gray_code += gray_code_bit
    
    return gray_code + "_"+GC


def main():
    print("\nConvert decimal to BCD")
    decimal = "123_" + BCD
    binary = decimal_to_BCD(decimal)
    print(f"decimal {decimal} is BCD {binary}")

    print("\nConvert binary to Gray Code")
    binary = "11101" + BASE_2
    gray_code = binary_to_gray_code(binary)
    print(f"binary {binary} is GC {gray_code}")





if __name__ == "__main__":
    main()