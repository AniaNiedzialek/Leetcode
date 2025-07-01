from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        current = head
        
        
        while current:
            # check if the current node is a duplicate
            if current.next and current.val == current.next.val:
                # store duplicated values
                dupl = current.val
                
                while current and current.val == dupl:
                    current = current.next
            
            else:
                current = current.next
                prev = prev.next
                
        return dummy.next
                