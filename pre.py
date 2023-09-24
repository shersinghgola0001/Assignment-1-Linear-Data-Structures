#Q7. Write a program to convert prefix expression to infix expression.
def is_operator(char):
    return char in "+-*/"
def prefix_to_infix(prefix_expression):
    stack = []
    tokens = prefix_expression.split()
    for token in reversed(tokens):
        if token.isalnum():
            stack.append(token)  
        elif is_operator(token):
            operand1 = stack.pop()
            operand2 = stack.pop()
            new_expression = f"({operand1}{token}{operand2})"
            stack.append(new_expression)
    if len(stack) != 1:
        raise ValueError("Invalid prefix expression")
    return stack[0]
prefix_expr = "+ * 3 5 2"
infix_expr = prefix_to_infix(prefix_expr)
print("Infix Expression:", infix_expr) 
