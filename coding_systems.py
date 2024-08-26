"""
Coding systems

Binary Coded Decimal [BCD] each digit in decimal number is represented by a 4-bt binary number. 
represented as string "00010000_BCD"
"""
from conversions_number_systems import decimal_to_binary, strip_suffix, BASE_10

BCD = "BCD"

# if binary string is not 4 digits adds zeros to prefix, pass in withou suffix
def get_4_bits(binary):
    while len(binary) < 4:
        binary = "0" + binary
    return binary

def decimal_to_BCD(decimal):
    decimal_striped = strip_suffix(decimal)
    bcd_str = ""
    for digit in decimal_striped:
        digit_representation = (digit + BASE_10)

        print("Digit")
        print(digit_representation, decimal_to_binary(digit_representation))

        # convert singular digit to binary
        digit_binary_code = strip_suffix(decimal_to_binary(digit_representation))
        digit_binary_4_bits = get_4_bits(digit_binary_code)
        bcd_str += digit_binary_4_bits
    
    return bcd_str + "_"+BCD

def main():
    print("\nConvert decimal to BCD")
    decimal = "123_" + BCD
    binary = decimal_to_BCD(decimal)
    print(f"decimal {decimal} is BCD {binary}")




if __name__ == "__main__":
    main()