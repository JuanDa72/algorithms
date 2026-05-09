# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(node1, node2):

            if not node1 or not node2:
                return None


            new_next=node2.next
            node1.next.next=node1
            node1.next=new_next

            new_node1=None
            new_node2=None
            if node1.next:
                new_node1=node1.next

            if node1.next.next:
                new_node2=node1.next.next

            swap(new_node1, new_node2)
            return node2

        return swap(head, head.next)


s=Solution()
head=ListNode()
print(s.swapPairs())