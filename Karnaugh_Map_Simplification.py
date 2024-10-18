"""
A Karnaugh map (K-map) is a visual method used to simplify the algebraic expressions in Boolean functions without having to resort to complex theorems or equation manipulations.



"""

class K_Map:

    def __init__(self, vars, minterms):
        self.vars  = vars   # 3 variable, 4 variable map
        self.minterms = minterms  # [0, 1, 5, 7]


        self.grid = []  # 2d-list
        self.init_grid()  # 2D-list
        self.place_minterms()

    def init_grid(self):
        # if var=4, then 4 cosl 4 rows
        # if var=3, then 4 cols 2 rows
        # if var=2, then 2 cols 2 rows

        num_rows, num_cols = 0, 0
        if self.vars == 3:
            num_rows, num_cols = 2, 4
        if self.vars == 2:  # check minterms of this
            num_rows, num_cols = 2, 2
        if self.vars == 4:
            num_rows, num_cols = 4, 4

        
        for _ in range(num_rows):
                self.grid.append(["" for _ in range(num_cols)])

        all_ms = [0, 1, 3, 2, 4, 5, 7, 6, 12, 13, 15, 14, 8, 9, 11, 10]

        i = 0
        for a in range(len(self.grid)):
            for b in range(len(self.grid[a])):
                self.grid[a][b] += "-"+str(all_ms[i])
                i += 1

    def place_minterms(self):
        for a in range(len(self.grid)):
            for b in range(len(self.grid[a])):
                for m in self.minterms:
                    if str(m) in self.grid[a][b]:
                        self.grid[a][b] = "1"+ self.grid[a][b]
                        break # breka to avoid duplicate ones if m exists more than once in grid-string


    
    def show_grid(self):
        print(f"{self.minterms=}")
        for row in self.grid:
            print(row)


def main():
    minterms = [0,1,5,7]
    kmap = K_Map(vars=3,  minterms=minterms) 
    kmap.show_grid()

    # TBD: convert row-indx to 00, 01, 11, 10. 
    # TBD: place 1 in minterm cells

if __name__ == "__main__":
    main()

            
