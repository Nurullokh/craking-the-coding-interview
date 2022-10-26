"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
"""

def intersection(headA, headB):
    if headA is None or headB is None:
            return None

    pa = headA 
    pb = headB

    while pa is not pb:
        if pa is None:
            pa = headB 
        else:
            pa=pa.next
        if pb is None:
            pb = headA 
        else:
            pb=pb.next

    return pa