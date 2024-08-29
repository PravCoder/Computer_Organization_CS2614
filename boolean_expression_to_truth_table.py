"""
Boolean Expression Evaluator
converts boolean expression -> truth table
only works for 2 inputs
"""
from logic_gates import AND_GATE, OR_GATE, NOT_GATE
import itertools, re


alpha = ["A","B","C","D"]

class BooleanExpression_TruthTable_Converter:

    def __init__(self, num_inputs, expression):
        self.num_inputs = num_inputs
        self.table = []
        self.init_empty()
        self.expression = expression
        self.command_value_dict = {}  # {command-id:0/1}
        # init dict
        self.set_dict()

    def init_empty(self):
        num_rows = 2 ** self.num_inputs  # formula for number of rows given number of inputs
        self.table.append([])  # add header row of table
        for input in range(self.num_inputs):  # iterate every input index and add a input header for that input
            self.table[0].append(alpha[input])      # add col header to header-row which is 0th row
        self.table[0].append(alpha[self.num_inputs])  # add the output header

        # iterate every acutal non-header row 
        for _ in range(num_rows): # add a row of zeros for each input-col plus one for the output column
            self.table.append([0 for _ in range(self.num_inputs+1)])

        combinations = list(itertools.product([0, 1], repeat=self.num_inputs)) # get all possible combination of inputs 0/1's like [(0, 0), (0, 1), (1, 0), (1, 1)]
        for i, combination in enumerate(combinations):  # iterate every combination of inputs
            for j, input_val in enumerate(combination):  # iterate the values in order of the current combination
                self.table[i+1][j] = input_val   # in table set ith row +1 offset for header and jth input-col equal to current input-value in the current combination
        

    def show(self):
        for row in self.table:
            print(row)

    def set_dict(self):
        for command in self.expression:
            self.command_value_dict[command[0]] = None
    
    def get_command_id_inputs(self, command):
        
        paran_indx = command.index("(")
        input1 = command[paran_indx+1]
        input2 = command[paran_indx+3]
        id = command[0]
        gate = ""
        if "AND" in command:
            gate = "AND"
        else:
            gate = "OR"

        return id, input1, input2, gate
    
    def insert_all_outputs(self):
        for i, row in enumerate(self.table):  # iterate each combination/row of inputs and get its output evalute expression.
            if i!= 0:
                self.set_dict()
                A = row[0]
                B = row[1]
                output_C = self.evaluate_output(A, B)
                # print(f"***{A=}, {B=}, {output_C=}, {i=}")
                self.table[i][2] = output_C
    
    def evaluate_output(self, A, B):  # 0/1 inputs for a specific case
        # print(self.command_value_dict)
        # iterate every command in order of expression
        for command in self.expression:
            # get the id inputs and gate type specified in the command
            id, input1, input2, gate = self.get_command_id_inputs(command)
            
            x, y = None, None  # these are the numerical 0/1 inputs of the current command
            if input1 == "A":  # if the specified input is a letter, then pass in the value that this function got 0/1
                x = A
            if input1 == "B":
                x = B
            if input1.isnumeric():  # if the specified input is a number, then we need to get that output value of that comamnd-id which is stored in dict.
                x = self.command_value_dict[input1]
            if input1.isnumeric():
                x = self.command_value_dict[input1]
            
            if input2 == "A":
                y = A
            if input2 == "B":
                y = B
            if input2.isnumeric():
                y = self.command_value_dict[input2]
            if input2.isnumeric():
                y = self.command_value_dict[input2]

            out = ""  # compute output given that we have numerical inputs of current command.
            if gate == "AND":
                out = AND_GATE(x, y).C
            if gate == "OR":
                out = OR_GATE(x, y).C

            self.command_value_dict[id] = out

            # print(f"{id=}, {input1=}, {input2=}, {gate}")
            # print(f"Numerical inputs: {x=} {y=} {out=}\n")

      
        return self.command_value_dict["3"]



def main():
    # same as (A AND B) AND (A OR B), 
    # order matters each command has a id and the gate and the inputs, inputs can be A/B or the id of another command which the value of that command.
    bool_expression = ["1-AND(A,B)", "2-OR(A,B)", "3-AND(1,2)"] 
    tt = BooleanExpression_TruthTable_Converter(2, bool_expression)
    print(tt.expression)
    # tt.show()
    # tt.evaluate_output(1, 0)
    tt.insert_all_outputs()
    tt.show()

    # Expression #2 -> same as (A AND B) OR (A OR B), 
    bool_expression = ["1-AND(A,B)", "2-OR(A,B)", "3-OR(1,2)"] 
    tt = BooleanExpression_TruthTable_Converter(2, bool_expression)
    print(tt.expression)
    tt.insert_all_outputs()
    tt.show()

if __name__ == "__main__":
    main()