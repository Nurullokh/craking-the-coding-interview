class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.minimum = None

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
            self.minimum = data
        else:
            temp = Node(data)
            temp.next = self.top
            self.top = temp
            if self.minimum > data:
                self.minimum = data
    
    def peek(self):
        if self.top is None:
            return "Stack is empty!"
        else:
            return self.top.data
    
    def pop(self):
        if self.top is None:
            return "Stack is empty!"
        else:
            temp = self.top.data
            if self.top.next is None:
                self.top = None
            else:
                self.top = self.top.next
            return temp

    def is_empty(self):
        return self.top == None
    
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next    
    
    def min_stack(self):
        if self.top == None:
            return "Stack is empty!"
        return self.minimum

