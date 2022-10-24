def move_tail_to_head(head):
    if head and head.next:
        last = head
        second_to_last = None
        while last.next:
            second_to_last = last
            last = last.next
        last.next = head
        second_to_last.next = None
        head = last