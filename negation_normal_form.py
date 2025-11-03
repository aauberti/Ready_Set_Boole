class Node:
    def __init__(self, op, left=None, right=None):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left is None and self.right is None:
            return f"{self.op}"
        elif self.right is None:
            return f"({self.op}{self.left})"
        else:
            return f"({self.left}{self.op}{self.right})"


def parse_rpn(formula: str) -> str:
    stack = []
    valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!&|^>="
    for c in formula:
        if c not in valid_chars:
            return None
        if c.isalpha():
            stack.append(Node(c))
        elif c == "!":
            if not stack:
                return None
            stack.append(Node('!', stack.pop()))
        else:
            if len(stack) < 2:
                return None
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(c, left, right))
    if len(stack) != 1:
        return None
    return stack[0]


def eliminate_complex_ops(node):
    if node.op in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return node

    if node.op == '!':
        return Node('!', eliminate_complex_ops(node.left))

    left = eliminate_complex_ops(node.left)
    right = eliminate_complex_ops(node.right)

    if node.op == '^':
        return Node('&',
                    Node('|', left, right),
                    Node('|', Node('!', left), Node('!', right)))
    elif node.op == '>':
        return Node('|', Node('!', left), right)
    elif node.op == '=':
        return Node('|',
                    Node('&', Node('!', left), Node('!', right)),
                    Node('&', left, right))
    else:
        return Node(node.op, left, right)


def attribute_negation(node):
    if node.op in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return node

    if node.op == '!':
        child = node.left

        if child.op == '!':
            return attribute_negation(child.left)

        if child.op in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return node
        if child.op == '&':
            return attribute_negation(Node('|',
                                           Node('!', child.left),
                                           Node('!', child.right)))
        if child.op == '|':
            return attribute_negation(Node('&',
                                           Node('!', child.left),
                                           Node('!', child.right)))
    return Node(node.op, attribute_negation(node.left),
                attribute_negation(node.right))


def tree_to_rpn(node):
    if node.op in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return node.op

    if node.op == '!':
        return tree_to_rpn(node.left) + '!'

    return tree_to_rpn(node.left) + tree_to_rpn(node.right) + node.op


def negation_normal_form(formula: str) -> str:
    tree = parse_rpn(formula)
    if tree is not None:
        tree = eliminate_complex_ops(tree)
        tree = attribute_negation(tree)
        return (tree_to_rpn(tree))
    else:
        print("Error")
        return None


def main():
    print(negation_normal_form("ABC&&!"))
    print("---------------------------")
    print(negation_normal_form("AB|!"))
    print("---------------------------")
    print(negation_normal_form("AB>"))
    print("---------------------------")
    print(negation_normal_form("AB="))
    print("---------------------------")
    print(negation_normal_form("AB|C&!"))


if __name__ == "__main__":
    main()
