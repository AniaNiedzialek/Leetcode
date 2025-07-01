
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # dummy node set to the beginning of the list
        dummy = ListNode(0, head)
        left = dummy
        right = head
        slow = head
        

        # get lengthh
        length = 0
        while right:
            length += 1
            right = right.next
        if length == 0 or k == 0:
            return head
        # set new k 
       
        k = k % length
        if k == 0:
            return head
        # reset the right pointer
        right = head
        # print(k)
        tmp = length - k - 1
        # print(tmp)
        
        for i in range(tmp ):
            if slow:
                slow = slow.next
        # print(slow.val)
        tmp2 = slow.next
        # print(tmp2)
        slow.next = None

        tail = tmp2
        while tail.next:
            tail = tail.next
        tail.next = head
      
        return tmp2

