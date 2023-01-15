class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            temp = Node(data)
            temp.next = self.top
            self.top = temp
    
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

s = Stack()
# print(s.peek())
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.pop()
s.pop()
s.pop()
s.push(4)
s.print_stack()
print(s.is_empty())
# print(s.peek())
