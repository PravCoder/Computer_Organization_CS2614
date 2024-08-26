"""
Complements

(r-1)'s complement
2's complement
"""

from conversions_number_systems import decimal_to_binary, strip_suffix, BASE_10, BASE_2


BASE_10_MAX = 99
BASE_8_MAX = 77  # octal
BASE_2_MAX = "11111_2"  # binary

def r_minus_1s_complement(number):
    # decimal number
    if "_10" in number:
        number = int(strip_suffix(number))
        difference = BASE_10_MAX - number
        return str(difference) + BASE_10
    # octal number
    if "_8" in number:
        pass
    # binary number
    if "_2" in number:
        pass

def main():
    print("\nCompute (r-1)'s complement")
    decimal = "57" + BASE_10
    r_m_1_comp = r_minus_1s_complement(decimal)
    print(f"decimal {decimal}'s (r-1)'s complement is {r_m_1_comp}")






if __name__ == "__main__":
    main()