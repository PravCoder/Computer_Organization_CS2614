"""
A Karnaugh map (K-map) is a visual method used to simplify the algebraic expressions in Boolean functions without having to resort to complex theorems or equation manipulations.



"""

class K_Map:

    def __init__(self, vars, minterms):
        self.vars  = vars   # 3 variable, 4 variable map
        self.minterms = minterms  # [0, 1, 5, 7]


        self.grid = []  # 2d-list
        self.init_grid()  # 2D-list

    def init_grid(self):
        # if var=4, then 4 cosl 4 rows
        # if var=3, then 4 cols 2 rows
        # if var=2, then 2 cols 2 rows

        num_rows, num_cols = 0, 0
        if self.vars == 3:
            num_rows, num_cols = 2, 4

        
        for _ in range(num_rows):
                self.grid.append(["" for _ in range(num_cols)])

        all_ms = [0, 1, 3, 2, 4, 5, 7, 6, 12, 13, 15, 14, 8, 9, 11, 10]

        i = 0
        for a in range(len(self.grid)):
            for b in range(len(self.grid[a])):
                self.grid[a][b] += str(all_ms[i])
                i += 1


    
    def show_grid(self):
         for row in self.grid:
            print(row)


def main():
    kmap = K_Map(vars=3, minterms=[0,1,5,7])
    kmap.show_grid()

if __name__ == "__main__":
    main()

            
