from linked_list import llist

# iterative approach
def reverse_iteratively(head):
    if not head:
        return 
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt 
    return prev
# Time complexity is O(n)
# Space complexity is O(1)

item = reverse_iteratively(llist.head)
while item:
    print(item.val)
    item = item.next

