

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None
    


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr


    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def add_after_node(self, key, data):
        curr = self.head
        while curr:
            if curr.next is None and curr.data == key:
                self.append(data)
                return
            elif curr.data == key:
                new_node = Node(data)
                nxt = curr.next
                curr.next = new_node
                new_node.next = nxt
                new_node.prev = curr
                nxt.prev = new_node
                return
            curr = curr.next
        
    def add_before_node(self, key, data):
        curr = self.head
        while curr:
            if curr.prev is None and curr.data == key:
                self.prepend(data)
                return
            elif curr.data == key:
                new_node = Node(data)
                prev = curr.prev
                prev.next = new_node
                curr.prev = new_node
                new_node.next = curr
                new_node.prev = prev
                return
            curr = curr.next
    