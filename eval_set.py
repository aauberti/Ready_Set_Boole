def eval_set(formula: str, sets: list[set[int]]) -> list[int]:

    sets = [set(s) for s in sets]
    global_set = set().union(*sets)
    stack = []

    bin_op_2 = '&|^'
    bin_op_3 = '>='

    dict_op = {
        '&': lambda a, b: a & b,
        '|': lambda a, b: a | b,
        '^': lambda a, b: a ^ b,
        '>': lambda a, b, global_set=None: (global_set - a) | b,
        '=': lambda a, b, global_set=None: global_set - (a ^ b),
        '!': lambda a, global_set=None: global_set - a
    }
    try:
        for op in formula:
            if op.isalpha():
                index = ord(op) - ord('A')
                stack.append(sets[index])
            elif op in bin_op_2:
                assert len(stack) >= 2, "Error"
                b = stack.pop()
                a = stack.pop()
                stack.append(dict_op[op](a, b))
            elif op in bin_op_3:
                assert len(stack) >= 2, "Error"
                b = stack.pop()
                a = stack.pop()
                stack.append(dict_op[op](a, b, global_set))
            elif op == '!':
                assert len(stack) >= 1, "Error"
                a = stack.pop()
                stack.append(dict_op[op](a, global_set))
        if len(stack) == 1:
            return list(stack[-1])
        else:
            print("Error")
            return None
    except AssertionError as ae:
        print(ae)
        return None


def main():
    a_set = [0, 1, 2]
    b_set = {0, 3, 4}
    print(eval_set("AB&", [a_set, b_set]))
    print("----")

    c_set = [0, 1, 2]
    d_set = {3, 4, 5}
    print(eval_set("AB|", [c_set, d_set]))
    print("----")

    e_set = {0, 1, 2}
    print(eval_set("A!", [e_set]))


if __name__ == '__main__':
    main()
