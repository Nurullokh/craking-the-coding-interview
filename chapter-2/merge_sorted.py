from linked_list import LinkedList
A = LinkedList()
A.append("1")
A.append("5")
A.append("6")
A.append("8")

B = LinkedList()
B.append("2")
B.append("3")
B.append("4")
B.append("7")

def merge_sorted(l_1, l_2):
    p = l_1.head
    q = l_2.head
    s = None
    if not p:
        return q
    if not q:
        return p

    if p and q:
        if p.val <= q.val:
            s = p
            p = s.next
        else:
            s = q
            q = q.next
        new_head = s
    while p and q:
        if p.val <= q.val:
            s.next = p
            s = p
            p = s.next
        else:
            s.next = q
            s = q
            q = s.next
        
    if not p:
        s.next = q
    if not q:
        s.next = p

    return new_head

# Time complexity is O(n)
new_head = merge_sorted(A, B)
while new_head:
    print(new_head.val)
    new_head = new_head.next

    