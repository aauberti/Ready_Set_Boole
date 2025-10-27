import itertools
import string 

def print_truth_table(formula: str):
    valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!&|^>="
    binary_ops = "&|^>="
    stack = []
    ops = []
    dict_op = {
        '&': lambda a, b: a & b,
        '|': lambda a, b: a | b,
        '^': lambda a, b: a ^ b,
        '>': lambda a, b: not(a) or b,
        '=': lambda a, b: a == b,
        '!': lambda a: not a
    }
    
    for c in formula:
        if c not in valid_chars:
            print("Wrong input")
            return None
        
    all_variables = [c for c in formula if c.isalpha()]
    if len(all_variables) != len(set(all_variables)):
        print("Error: Duplicate variables found")
        return None
    
    variables = tuple(c for c in formula if c.isalpha())
    nb_vars = len(variables)
        
    if nb_vars == 0:
        print("No variables found")
        return None

    var_values_test = {var: 0 for var in variables}
    stack_test = []
    
    for c in formula:
        if c.isalpha():
            stack_test.append(var_values_test[c])
        elif c == '!':
            if len(stack_test) < 1:
                print("Invalid formula")
                return None
            stack_test.pop()
            stack_test.append(0)
        elif c in binary_ops:
            if len(stack_test) < 2:
                print("Invalid formula")
                return None
            stack_test.pop()
            stack_test.pop()
            stack_test.append(0)
    
    if len(stack_test) != 1:
        print("Invalid formula")
        return None

    header = " | ".join(variables) + " | " + '='
    print("| " + header + " |")
    print("|" + "|".join(["---"] * (nb_vars + 1)) + "|")
        
    for combination in itertools.product([0, 1], repeat=nb_vars):

        var_values = dict(zip(variables, combination))
        stack = []
        
        for c in formula:
            if c.isalpha():
                stack.append(var_values[c])
            elif c == '!':
                if len(stack) < 1:
                    print("Error: not enough operands")
                    return None
                a = stack.pop()
                stack.append(dict_op['!'](a))
            elif c in binary_ops:
                if len(stack) < 2:
                    print("Error: not enough operands")
                    return None
                b = stack.pop()
                a = stack.pop()
                stack.append(dict_op[c](a, b))

        result = stack[0]     
        row = " | ".join(map(str, combination)) + " | " + str(int(result))
        print("| " + row + " |")

def main():
    print_truth_table("AB&A|")
    print("-------------------------")
    print_truth_table("POJ||")
    print("-------------------------")
    print_truth_table("FTG>&")
    print("-------------------------") 
    print_truth_table("AW==")
    print("-------------------------")
    print_truth_table("WERTY||=")

if __name__ == "__main__":
    main()