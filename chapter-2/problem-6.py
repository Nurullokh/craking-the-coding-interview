"""
Palindrome: Implement a function to check if a linked list is a palindrome
"""

# solution 1 using string
def is_palindrome1(node):
    s = ""
    while node:
        s += node.data
        node = node.next
    return s == s[::-1]

# solution 2 using stack
def is_palindrome2(node):
    stack = []
    p = node
    while p:
        stack.append(p.data)
        p = p.next
    p = node
    while p:
        if stack.pop() != p.data:
            return False
        p = p.next
    return True

# solution 3 using 2 pointers
def is_palindrome3(head):
    if head:
        p = head
        q = head
        prev = []
        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1
        q = prev[i-1]
        count = 1
        while count <= i // 2 + 1:
            if prev[-count] != p.val:
                return False
            p = p.next
            count += 1
        return True
    else:
        return False

# solution 4 with reversing
def is_palindrome4(node):
    def reverse(node):
        if not node:
            return
        prev = None
        curr = node
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    reversed = reverse(node)
    while node and reversed:
        if reversed.data != node.data:
            return False
        reversed = reversed.next
        node = node.next
    return True

