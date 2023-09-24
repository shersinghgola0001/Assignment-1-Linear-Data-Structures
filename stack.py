#Q10. Write a program to find the smallest number using a stack.
class MinStack:
    def __init__(self):
        self.data_stack = []  
        self.min_stack = []   
    def push(self, item):
        self.data_stack.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)
    def pop(self):
        if not self.data_stack:
            raise IndexError("Pop from an empty stack")
        item = self.data_stack.pop()
        if item == self.min_stack[-1]:
            self.min_stack.pop()
        return item
    def get_min(self):
        if not self.min_stack:
            raise IndexError("Get minimum from an empty stack")
        return self.min_stack[-1]
stack = MinStack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(1)
print("Smallest Number:", stack.get_min())  
