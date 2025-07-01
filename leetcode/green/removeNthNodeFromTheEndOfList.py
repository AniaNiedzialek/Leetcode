

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

    # Test case 1: Remove 2nd node from end from [1,2,3,4,5]
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result1 = solution.removeNthFromEnd(head1, 2)
    print_linked_list(result1)  # Expected: [1, 2, 3, 5]

    # Test case 2: Remove 1st node from end from [1]
    head2 = ListNode(1)
    result2 = solution.removeNthFromEnd(head2, 1)
    print_linked_list(result2)  # Expected: []

    # Test case 3: Remove 1st node from end from [1,2]
    head3 = ListNode(1, ListNode(2))
    result3 = solution.removeNthFromEnd(head3, 1)
    print_linked_list(result3)  # Expected: [1]

    # Test case 4: Remove 2nd node from end from [1,2]
    head4 = ListNode(1, ListNode(2))
    result4 = solution.removeNthFromEnd(head4, 2)
    print_linked_list(result4)  # Expected: [2]