class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    
    def add(self, data):
        item = Node(data)
        if self.last != None:
            self.last.next = item
        self.last = item
        if self.first == None:
            self.first = self.last
    
    def remove(self):
        if self.first is None:
            return "Queue is empty!"
        data = self.first.data
        self.first = self.first.next
        if self.first == None:
            self.last == None
        return data

    def peek(self):
        if self.first == None:
            return "Queue is empty!"
        return self.first.data
    
    def is_empty(self):
        return self.first != None

    
    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.data)
            temp = temp.next
    

q = Queue()
# print(q.is_empty())
q.add(1)
q.add(2)
q.add(3)
q.add(4)
# q.remove()
# q.remove()
# q.remove()
# q.remove()
# q.remove()
# print(q.peek())
q.print_queue()