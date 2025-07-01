

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # set the n distance
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # shift pointers
        while right:
            right = right.next
            left = left.next

        # delete the node
        left.next = left.next.next
        
        return dummy.next