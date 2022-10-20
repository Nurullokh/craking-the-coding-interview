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
# # Example
# item = reverse_iteratively(llist.head)
# while item:
#     print(item.val)
#     item = item.next


# recursive approach
def reverse_recursively(head):
    def _reverse_recursively(curr, prev):
        if not curr:
            return prev
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

        return _reverse_recursively(curr, prev)
    
    return _reverse_recursively(curr=head, prev=None)
# time comlexity is O(n)
# space complexiyt is O(n)

# Example
item = reverse_recursively(llist.head)
while item:
    print(item.val)
    item = item.next



