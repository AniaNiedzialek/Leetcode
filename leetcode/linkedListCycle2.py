from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        seen = set() # to mark the visited nodes
        
        
        while curr:
            if curr in seen:
                return True # this is a cycle
            else:
                seen.add(curr)
                curr = curr.next
            
        return False # not a cycle  
    
solution = Solution()

head = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# point to the correct next node
head.next = node2
node2.next = node3
node3.next = node4 
node4.next = node2 # create a cycle


print(f" The result is: ", solution.hasCycle(head))

head2 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)

head.next = node2
node2.next = node3
# node3 points to None

print(f"The result now is: ", solution.hasCycle(head2))


