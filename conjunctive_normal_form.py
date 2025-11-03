from negation_normal_form import negation_normal_form, \
    parse_rpn, tree_to_rpn, Node


def distribute(node):
    if node.op in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or node.op == '!':
        return node

    if node.op == '&':

        return Node('&', distribute(node.left), distribute(node.right))

    if node.op == '|':
        left = distribute(node.left)
        right = distribute(node.right)

        if left.op == '&':
            return Node('&',
                        distribute(Node('|', left.left, right)),
                        distribute(Node('|', left.right, right)))

        if right.op == '&':
            return Node('&',
                        distribute(Node('|', left, right.left)),
                        distribute(Node('|', left, right.right)))

        return Node('|', left, right)

    return node


def conjunctive_normal_form(formula: str) -> str:
    formula = negation_normal_form(formula)
    if formula is not None:
        tree = parse_rpn(formula)
        tree = distribute(tree)
        return tree_to_rpn(tree)
    return None


def main():
    print(conjunctive_normal_form("ABA|&!"))
    print("----------------------")
    print(conjunctive_normal_form("AB|!"))
    print("----------------------")
    print(conjunctive_normal_form("AB|C&"))
    print("----------------------")
    print(conjunctive_normal_form("AB|C|D|"))
    print("----------------------")
    print(conjunctive_normal_form("AB&C&D&"))
    print("----------------------")
    print(conjunctive_normal_form("AB&!C!|"))
    print("----------------------")
    print(conjunctive_normal_form("AB|!C!&"))
    print("----------------------")


if __name__ == "__main__":
    main()
