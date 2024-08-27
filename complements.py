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

# write zeors for aech bit until you reach first one, then keep that one and after that one invert all bits. 
def r_2s_complement(binary):
    binary = strip_suffix(binary)
    r2s = ""
    found_first_one = False
    for i in range(len(binary)-1, -1, -1):  # iterate from right to left
        print(binary[i])
        if found_first_one == False:
            if binary[i] == "0":
                r2s += "0"
                continue
            if binary[i] == "1":
                r2s +=  "1"  # keep first one
                found_first_one = True
                print("YESS")
                continue
        if found_first_one == True:
            if binary[i] == "0":
                r2s += "1"
                continue
            if binary[i] == "1":
                r2s += "0"
                continue
    return r2s[::-1] + BASE_2  # reverse because we loop reverse and add to enw str-r2s

def main():
    print("\nCompute (r-1)'s complement")
    decimal = "57" + BASE_10
    r_m_1_comp = r_minus_1s_complement(decimal)
    print(f"decimal {decimal}'s (r-1)'s complement is {r_m_1_comp}")

    print("\nCompute 2's complement")
    binary = "11010" + BASE_2
    r_2s_comp = r_2s_complement(binary)
    print(f"binary {binary}'s r2's complement is {r_2s_comp}")






if __name__ == "__main__":
    main()