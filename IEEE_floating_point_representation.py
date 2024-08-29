
"""
Convert Decimal number to IEEE Floating Point Representation. A IEEE
number is represented as a string "0_10000001_11100000000000000000000".
Sign - 1 bit.
Exponent - 8 bits.
Mantissa - 24 bits.

"""

from conversions_number_systems import decimal_to_binary, floating_point_decimal_to_binary, strip_suffix, BASE_10, BASE_2
EXPONENT_BIAS = 127

# HELPER FUNCTIONS
def move_dot(number):  # moves dot to the right until there is on number on the right of it, also returns the exponent or the number of times dot was moved
    num_elements = [n for n in number]
    if num_elements[1] == ".": return number, 0
    old_indx = num_elements.index(".")

    num_elements.remove(".")
    num_elements.insert(1, ".")  
    new_indx = num_elements.index(".")

    moved_dot_number = "".join(num_elements) 
    number_of_times_moved = abs(new_indx - old_indx)
    return moved_dot_number, number_of_times_moved

def get_bits_before_dot(number):
    dot_indx =  number.index(".")
    return number[0:dot_indx] # exclusive
def get_bits_after_dot(number):
    dot_indx =  number.index(".")
    return number[dot_indx+1:] # exclusive

def decimal_to_floating_point_IEEE(N):
    N_ns = strip_suffix(N) # no suffix N
    N_binary = floating_point_decimal_to_binary(N)
    N_binary_before_dot_move = N_binary
    print(f"{N_binary_before_dot_move=}")

    N_binary, num_dot_moved = move_dot(N_binary)
    exponent = num_dot_moved + EXPONENT_BIAS  # int
    print(f"After dot move: {N_binary=}, {exponent=}")

    binary_exponent = decimal_to_binary(str(exponent)+BASE_10)
    if len(strip_suffix(binary_exponent)) == 7:  # add zero to get number correct 8 number of bits
        binary_exponent=  "0"+binary_exponent
    print(f"{binary_exponent=}")

    sign_bit = "1" if "-" in N else "0"  
    print(f"{sign_bit=}")

    bits_after_dot = get_bits_after_dot(N_binary)  # after moving the dot get the bits after the dot
    mantissa = ""+bits_after_dot
    mantissa = strip_suffix(mantissa)
    print(f"{mantissa=},     {N_binary_before_dot_move=}")
    while len(mantissa) < 23:  # keep adding zeros until we get 23-bits for mantissa
        mantissa += "0"   
    
    ieee_float = ""+sign_bit +"_"+ strip_suffix(binary_exponent) +"_"+ mantissa
    return ieee_float


def main():
    # Note doesn't work for negative decimals
    print("\Convert decimal to floating point representation IEEEs")
    decimal = "1.3" + BASE_10
    float = decimal_to_floating_point_IEEE(decimal)
    print(f"decimal {decimal}'s floating IEEE is {float}")





if __name__ == "__main__":
    main()