
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
# test cases

# ...existing code...

def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Rotate [1,2,3,4,5] by 2 -> [4,5,1,2,3]
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result1 = solution.rotateRight(head1, 2)
    print_linked_list(result1)  # Expected: [4, 5, 1, 2, 3]

    # Test case 2: Rotate [0,1,2] by 4 -> [2,0,1]
    head2 = ListNode(0, ListNode(1, ListNode(2)))
    result2 = solution.rotateRight(head2, 4)
    print_linked_list(result2)  # Expected: [2, 0, 1]

    