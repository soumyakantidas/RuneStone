from python.datastructures.DS import Stack


def infix_to_postfix(infix_expr):
    precedence = dict()
    precedence["*"] = 3
    precedence["/"] = 3
    precedence["+"] = 2
    precedence["-"] = 2
    precedence["("] = 1

    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_op = op_stack.pop()
            while top_op != '(':
                postfix_list.append(top_op)
                top_op = op_stack.pop()
        else:
            while op_stack.is_not_empty() and precedence[token] <= precedence[op_stack.peek()]:
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while op_stack.is_not_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)


def evaluate(infix_expr):
    post_fix_list = infix_to_postfix(infix_expr).split()
    operand_stack = Stack()

    for token in post_fix_list:
        if token in "0123456789":
            operand_stack.push(token)
        else:
            r_operand, l_operand = int(operand_stack.pop()), int(operand_stack.pop())
            result = do_math(l_operand, token, r_operand)
            operand_stack.push(result)

    return operand_stack.pop()


def do_math(l_operand, op, r_operand):
    if op == "+":
        return l_operand + r_operand
    elif op == "-":
        return l_operand - r_operand
    elif op == "*":
        return l_operand * r_operand
    else:
        return l_operand / r_operand


if __name__ == "__main__":
    print(infix_to_postfix("( 2 + 3 ) / ( 4 + 5 )"))
    print(evaluate("( 2 + 3 ) / ( 4 + 5 )"))
