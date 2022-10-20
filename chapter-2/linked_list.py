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
    
    # print the linked list one by one
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.val)
            cur_node = cur_node.next
    
    # prepend method
    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # insert method
    def insert(self, prev_node, data):
        if not prev_node:
            print("Error: you have to give previous node")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # delete by value
    def delete_node(self, key):
        curr_node = self.head

        # checking if key is equal to head
        if curr_node and curr_node.val == key:
            self.head = curr_node.next
            curr_node = None
            return
        prev = None
        while curr_node and curr_node.val != key:
            prev = curr_node
            curr_node = curr_node.next
        
        # check whether key is found or not
        if curr_node is None:
            return
        
        prev.next = curr_node.next
        curr_node = None
    

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
# llist.print_list() 

    