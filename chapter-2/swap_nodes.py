from linked_list import llist
import copy
def swap_nodes(val_1, val_2, head):
    if val_1 == val_2:
        return 
    prev_1 = None
    curr_1 = head
    while curr_1 and curr_1.val != val_1:
        prev_1 = curr_1
        curr_1 = curr_1.next
    prev_2 = None
    curr_2 = head
    while curr_2 and curr_2.val != val_2:
        prev_2 = curr_2
        curr_2 = curr_2.next
    
    
    if not curr_1 or not curr_2:
        return 
    
    if prev_1:
        prev_1.next = curr_2
    else:
        head = curr_2
    if prev_2:
        prev_2.next = curr_1
    else:
        head = curr_1
    curr_1.next, curr_2.next = curr_2.next, curr_1.next
    return head

head = swap_nodes("B", "D", llist.head)


