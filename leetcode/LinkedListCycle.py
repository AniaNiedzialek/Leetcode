from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

# Test case
solution = Solution()

# Create a linked list: 3 -> 2 -> 0 -> -4 -> (cycle back to 2)
head = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creates a cycle

print(solution.hasCycle(head))  # Output: True

# Create a linked list without a cycle: 1 -> 2 -> 3 -> None
head2 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

head2.next = node2
node2.next = node3

print(solution.hasCycle(head2))  # Output: False

# Time complexity: O(n)
# Space complexity: O(1)

