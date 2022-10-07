# A linked list is a data structure that represents a sequence of nodes.
# In a singley linked list, each node points to the next node in the linked list. 
# A boudbly linked list gives each node pointers to both the next and the previous nodes.


# Access time complexity is O(n)
# Inserting and deleting is O(1)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    # appending to the linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
    
