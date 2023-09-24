#Q9. Write a program to reverse a stack.
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")
    def size(self):
        return len(self.items)
def reverse_stack(stack):
    aux_stack = Stack()

    while not stack.is_empty():
        item = stack.pop()
        aux_stack.push(item)
    return aux_stack
original_stack = Stack()
original_stack.push(1)
original_stack.push(2)
original_stack.push(3)
original_stack.push(4)
reversed_stack = reverse_stack(original_stack)
print("Original Stack:")
while not original_stack.is_empty():
    print(original_stack.pop())
print("Reversed Stack:")
while not reversed_stack.is_empty():
    print(reversed_stack.pop())
