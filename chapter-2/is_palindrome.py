from linked_list import LinkedList

# solution 1 using string
def is_palindrome1(head):
    s = ""
    while head:
        s += head.val
        head = head.next
    return s == s[::-1]

# solution 2 using stack
def is_palindrome2(head):
    p = head
    s = []
    while p:
        s.append(p.val)
        p = p.next
    p = head
    while p:
        data = s.pop()
        if data != p.val():
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