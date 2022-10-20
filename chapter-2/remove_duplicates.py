from linked_list import LinkedList
A = LinkedList()
A.append(1)
A.append(2)
A.append(3)
A.append(2)
A.append(4)
A.append(3)
A.print_list()

print("-----------")

def remove_dups(head):
    curr = head
    prev = None
    dup_values = {}

    while curr:
        if curr.val in dup_values:
            prev.next = curr.next
            curr = None
        else:
            dup_values[curr.val] = 1
            prev = curr
        curr = prev.next
    
    return head

# Time complexity is O(n)
node_without_dups = remove_dups(A.head)
while node_without_dups:
    print(node_without_dups.val)
    node_without_dups = node_without_dups.next
