def find_beginning(head):
    if not head:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    
    if fast is None or fast.next is None:
        return
    
    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return fast