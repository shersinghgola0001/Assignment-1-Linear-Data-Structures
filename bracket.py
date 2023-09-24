#Q8. Write a program to check if all the brackets are closed in a given code snippet.
def bracket_closed(code_snippet):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    for char in code_snippet:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != bracket_pairs[char]:
                return False
    return len(stack) == 0
code = """def example_function():
    if (x > 0) {
        return [1, 2, 3];
    } else {
        return (a + b);
    }
}"""
result = bracket_closed(code)
if result:
    print("All brackets are closed properly.")
else:
    print("Not all brackets are closed properly.")
