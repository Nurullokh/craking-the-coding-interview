from length import len_iterative
from linked_list import llist


# first approach with knowing the length
def print_nth_from_last(head, n):
    total_len = len_iterative(head)

    curr = head
    while curr:
        if total_len == n:
            return curr.val
        
        total_len -= 1 
        curr = curr.next

    if curr is None:
        return 
    
# Time complexity is O(n)

# print(print_nth_from_last(llist.head, 2))

# second approach
def print_nth_from_last2(head, n):
    p = head
    q = head
    if n > 0:
        count = 0
        while q:
            count += 1
            if count >= n:
                break
            q = q.next
        
        if not q:
            return 
        
        while p and q.next:
            p = p.next
            q = q.next

        return p.val
    else:
        return None




