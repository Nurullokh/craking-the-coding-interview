"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input:(7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
"""
from linked_list import Node
def sum_lists(node1, node2, carry):
    if not nod1 and not node2 and carry == 0:
        return 
    result = Node(None)
    value = carry
    if node1:
        value += node1.data
    if node2:
        value += node2.data
    result.data = value % 10
    if node1 or node2:
        more = None
        if value >= 10:
            value = 1
        else:
            value = 0
        if node1 and node2:
            more = sum_lists(node1.next, node2.next, value)
        elif node1:
            more = sum_lists(nod1.next, None, value)
        else:
            more = sum_lists(None, node2.next, value)
        result.next = more
    return result