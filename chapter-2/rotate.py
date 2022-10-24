from linked_list import llist

def rotate(head, k):
    if head and head.next:
        p = head
        q = head
        prev = None
        count = 0

        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev

        while q:
            prev = q
            q = q.next

        q = prev
        q.next = head
        head = p.next
        p.next = None

    return head

node = rotate(llist.head, 3)
while node:
    print(node.val)
    node = node.next

    