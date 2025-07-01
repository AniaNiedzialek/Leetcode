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
                prev.next = current
            else:
                current = current.next
                prev = prev.next
                
        return dummy.next
                
                
# test case

# ...existing code...

def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

if __name__ == "__main__":
    solution = Solution()

    # Test case 1: [1,2,3,3,4,4,5] -> [1,2,5]
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
    result1 = solution.deleteDuplicates(head1)
    print_linked_list(result1)  # Expected: [1, 2, 5]

    # Test case 2: [1,1,1,2,3] -> [2,3]
    head2 = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
    result2 = solution.deleteDuplicates(head2)
    print_linked_list(result2)  # Expected: [2, 3]

    # Test case 3: [1,1,2,2] -> []
    head3 = ListNode(1, ListNode(1, ListNode(2, ListNode(2))))
    result3 = solution.deleteDuplicates(head3)
    print_linked_list(result3)  # Expected: []

    # Test case 4: [1,2,3] -> [1,2,3]
    head4 = ListNode(1, ListNode(2, ListNode(3)))
    result4 = solution.deleteDuplicates(head4)
    print_linked_list(result4)  # Expected: [1, 2, 3]

    # Test case 5: [] -> []
    head5 = None
    result5 = solution.deleteDuplicates(head5)
    print_linked_list(result5)  # Expected: []