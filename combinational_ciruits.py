"""
Combinational Ciruits
"""
class HALF_ADDER:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.carry, self.s = self.truth_table()

    def truth_table(self):
        carry, s = 0, 0
        if self.x == 0 and self.y == 0:
            carry = 0
            s = 0
        if self.x == 0 and self.y == 1:
            carry = 0
            s = 1
        if self.x == 1 and self.y == 0:
            carry = 0
            s = 1
        if self.x == 1 and self.y == 1:
            carry = 1
            s = 1
        return carry, s
    
    def compute(self, x, y):
        self.x, self.y = x, y
        self.carry, self.s = self.truth_table()
        return self.carry, self.s
    

def main():
    print("HALF ADDER TESTING")
    hf = HALF_ADDER(0, 1)
    print(f"x={hf.x} and y={hf.y} then carry={hf.carry} sum={hf.s}")

if __name__ == "__main__":
    main()