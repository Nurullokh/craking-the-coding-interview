"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input:3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
Output:3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""

def partition(head, x):
    befor_start = None
    before_end = None
    after_start = None
    after_end = None

    while head:
        nxt = head.next
        head.next = None

        if head.data < x:
            if befor_start is None:
                befor_start = head
                before_end = befor_start
            else:
                before_end.next = head
                before_end = head
        else:
            if after_start is None:
                after_start = head
                after_end = after_start
            else:
                after_end.next = head
                after_end = head
        head = nxt 
    if befor_start is None:
        return after_start
    before_end.next = after_start
    return befor_start
