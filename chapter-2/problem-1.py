"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""
# Solution 1 with buffer
from linked_list import LinkedList


def remove_dups(head: LinkedList) -> LinkedList:
    node = head
    if not node:
        return 
    dc = {}
    prev = None
    while node:
        if node.val in dc:
            prev.next = node.next
        else:
            dc[node.val] = 1
            prev = node
        node = node.next
    return head
# Time complexity is O(N)
# Space complexity is O(N)

l = LinkedList()
l.append("1")
l.append("2")
l.append("2")
l.append("3")
l.append("4")
res = remove_dups(l.head)
while res:
    print(res.val)
    res = res.next


# Solution 2 without buffer
def remove_dups2(head: LinkedList) -> LinkedList:
    curr_node = head
    while cur_node:
        runner = cur_node
        while runner.next:
            if runner.next.val == cur_node.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        cur_node = cur_node.next

# Time complexity is O(N ** 2)
# Space comlexity is O(1)





