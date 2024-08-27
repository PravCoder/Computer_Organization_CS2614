
"""
Convert Decimal number to IEEE Floating Point Representation. A IEEE
number is represented as a string "0_10000001_11100000000000000000000".
Sign - 1 bit.
Exponent - 8 bits.
Mantissa - 24 bits.

"""

from conversions_number_systems import decimal_to_binary, floating_point_decimal_to_binary, strip_suffix, BASE_10, BASE_2

# HELPER FUNCTIONS
def move_dot(number):  # moves dot to the right until there is on number on the right of it
    num_elements = [n for n in number]
    if num_elements[1] == ".": return number
    old_indx = num_elements.index(".")

    num_elements.remove(".")
    num_elements.insert(1, ".")  
    new_indx = num_elements.index(".")

    moved_dot_number = "".join(num_elements) 
    number_of_times_moved = abs(new_indx - old_indx)
    return moved_dot_number, number_of_times_moved

def decimal_to_floating_point_IEEE(N):
    N_ns = strip_suffix(N) # no suffix N
    N_binary = floating_point_decimal_to_binary(N)
    print(N_binary)
    N_binary, exponent = move_dot(N_binary)
    print(N_binary, exponent)

def main():
    print("\nCompute decimal to floating point representation IEEEs")
    decimal = "7.5" + BASE_10
    float = decimal_to_floating_point_IEEE(decimal)
    print(f"decimal {decimal}'s floating IEEE is {float}")





if __name__ == "__main__":
    main()