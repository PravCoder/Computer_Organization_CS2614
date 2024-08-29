
class AND_GATE:

    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.C = self.truth_table()
        self.type = "and"
    
    def truth_table(self):
        if self.A == 0 and self.B == 0:
            return 0
        if self.A == 0 and self.B == 1:
            return 0
        if self.A == 1 and self.B == 0:
            return 0
        if self.A == 1 and self.B == 1:
            return 1
    
    def compute(self, x, y):
        self.A, self.B = x, y
        self.C = self.truth_table()
        return self.C
    
        

def main():
    print("AND GATE TESTING")
    gate1 = AND_GATE(1, 1)
    print(f"A={gate1.A} and B={gate1.B} then C={gate1.C}")
    gate1.compute(0, 0)
    print(f"A={gate1.A} and B={gate1.B} then C={gate1.C}")
    gate1.compute(0, 1)
    print(f"A={gate1.A} and B={gate1.B} then C={gate1.C}")
    gate1.compute(1, 0)
    print(f"A={gate1.A} and B={gate1.B} then C={gate1.C}")

if __name__ == "__main__":
    main()