class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.minimum = None
    
    def append(self, value) -> None:
        if self.stack:
            self.minimum = value
        else:
            if self.minimum > value:
                self.minimum = value
        self.stack.append(value)
    
    def peek(self) -> int:
        if self.stack:
            return self.stack[-1]
        return "Stack is empty"
    
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        return "Stack is empty"
    
    def min_stack(self):
        if self.stack:
            return self.minimum
        return "Stack is empty"

