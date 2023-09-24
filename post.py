#Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression
def postfix_to_prefix(postfix_expression):
    stack = []
    for token in postfix_expression:
        if token.isalnum():
            stack.append(token)  
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            new_expression = token + operand1 + operand2
            stack.append(new_expression)
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    return stack[0]
postfix_expr = "35+"
prefix_expr = postfix_to_prefix(postfix_expr)
print("Prefix Expression:", prefix_expr) 
