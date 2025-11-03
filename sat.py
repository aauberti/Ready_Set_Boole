import itertools


def truth_table(formula: str) -> bool | None:
    valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!&|^>="
    binary_ops = "&|^>="
    stack = []
    dict_op = {
        '&': lambda a, b: a & b,
        '|': lambda a, b: a | b,
        '^': lambda a, b: a ^ b,
        '>': lambda a, b: not (a) or b,
        '=': lambda a, b: a == b,
        '!': lambda a: not a
    }

    for c in formula:
        if c not in valid_chars:
            print("Wrong input")
            return None

    variables = tuple(c for c in formula if c.isalpha())
    nb_vars = len(variables)

    if nb_vars == 0:
        print("No variables found")
        return None

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

        if len(stack) != 1:
            print("Error: invalid formula")
            return None

        if stack[0]:
            return True
    return False


def sat(formula: str) -> str:
    if formula is not None:
        return truth_table(formula)
    return None


def main():
    print(sat("AB|"))
    print("----------------")
    print(sat("AB&"))
    print("----------------")
    print(sat("AA!&"))
    print("----------------")
    print(sat("AA^"))
    print("----------------")
    print(sat("AB&C|"))


if __name__ == "__main__":
    main()
