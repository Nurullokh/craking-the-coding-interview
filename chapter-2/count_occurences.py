from linked_list import llist 

# iterative approach
def count_occurences(head, val):
    count = 0
    curr = head
    while curr:
        if curr.val == val:
            count += 1
        curr = curr.next
    return count

# TC - O(n)
# SC - O(1)

# recursive approach
def count_occurences_rec(node, val):
    if not node:
        return 0
    if node.val == val:
        return 1 + count_occurences_rec(node.next, val)
    else:
        return count_occurences_rec(node.next, val)

# TC - O(n)
# SC - O(n)