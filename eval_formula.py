def eval_formula(formula: str) -> bool:
    symbol = "01!&|^>="
    operator = "!&|^>="
    stack = []

    dict_op = {
        '!': lambda a, b: a != b,
        '&': lambda a, b: a & b,
        '|': lambda a, b: a | b,
        '^': lambda a, b: a ^ b,
        '>': lambda a, b: not(a) or b,
        '=': lambda a, b: a == b
    }
    for c in formula:
        if c not in symbol :
            print("Wrong input")
            return None
        if c in operator:
            if len(stack) < 2:
                print("Error: not enough operands")
                return None
            b = stack.pop()
            a = stack.pop()
            stack.append(dict_op[c](a, b))
        elif c in "01":
            stack.append(bool(int(c)))
    if len(stack) == 1:
        return stack[0]
    else:
        print("Error: invalid formula")
        return None

def main():
    print(eval_formula("10&"))
    print(eval_formula("10|"))
    print(eval_formula("11>"))
    print(eval_formula("10="))
    print(eval_formula("10111||="))

if __name__ == "__main__":
    main()