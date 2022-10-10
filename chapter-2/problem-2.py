"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""
from linked_list import LinkedList, Node

def return_kth_to_last(head: LinkedList, k: int):
    def height(head: LinkedList) -> int:
        if not head:
            return 0
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    
    h = height(head)
    diff = h - k
    c = 0
    while head:
        c += 1
        if diff == c:
            return head.val
        else:
            head = head.next
    return "There is no such value in the given linked list"

l = LinkedList()
l.append("1")
l.append("2")
l.append("3")
l.append("4")
print(return_kth_to_last(l.head, 1))
print(return_kth_to_last(l.head, 0))
print(return_kth_to_last(l.head, 2))
print(return_kth_to_last(l.head, 3))
print(return_kth_to_last(l.head, 4))
print(return_kth_to_last(l.head, 10))


# Another cooler approach

def kth_to_last(head: LinkedList, k: int) -> Node:
    p1, p2 = head, head

    # Move p1 k nodes into the list
    for i in range(k):
        if not p1:
            return 
        p1 = p1.next
    # Move them at the same space. When p1 hits the end, p2 will be
    # at the right element
    while p1:
        p1 = p1.next
        p2 = p2.next
    retunr p2
            
