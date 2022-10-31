

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
        pass

    def print_list(self):
        pass