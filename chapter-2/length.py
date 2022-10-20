from linked_list import llist

# iterative approach
def len_iterative(head):
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count

# Time complexity is O(n)
# Space complexity is O(1)

# print(len_iterative(llist.head))

# recursive approach
def len_recursive(head):
    if head is None:
        return 0
    return 1 + len_recursive(head.next)

print(len_recursive(llist.head))
