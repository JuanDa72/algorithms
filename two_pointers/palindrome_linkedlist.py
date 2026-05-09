class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head) -> bool:
    pointer = head
    stack: list[int] = []
    while pointer != None:
        stack.append(pointer.val)
        pointer = pointer.next

    for i in range(len(stack) - 1, -1, -1):
        if stack[i] != head.val:
            return False

        head = head.next

    return True

print(isPalindrome([1,2,2,1]))