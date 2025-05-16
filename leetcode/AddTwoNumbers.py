from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0) # temporary started node
        current = dummy
        carry = 0
    
        while l1!= None or l2 != None or carry != 0:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0    
            sum_res = l1_val + l2_val + carry
            carry = sum_res // 10
            newNode = ListNode(sum_res % 10)
            current.next = newNode
            current = newNode
            # add_digits(l1, l2)
           
            # current.next = ListNode(sum_res) # attach the new node
            # current = current.next # move the pointer
            # update the inputs
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
            
        # print(dummy.next.val)
        
        return dummy.next

# Test cases for AddTwoNumbers
def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    """Helper function to print a linked list."""
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values))

# Test case 1: 342 + 465 = 807
l1 = create_linked_list([2, 4, 3])  # Represents 342
l2 = create_linked_list([5, 6, 4])  # Represents 465

curr = l1
curr2 = l2

while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")

while curr2:
    print(curr2.val, end=" -> ")
    curr2 = curr2.next
print("None")

solution = Solution()
result = solution.addTwoNumbers(l1, l2)


print("Test Case 1:")
print_linked_list(result)  # Expected Output: 7 -> 0 -> 8

# Test case 2: 0 + 0 = 0
l1 = create_linked_list([0])  # Represents 0
l2 = create_linked_list([0])  # Represents 0
result = solution.addTwoNumbers(l1, l2)
print("Test Case 2:")
print_linked_list(result)  # Expected Output: 0

# Test case 3: 999 + 1 = 1000
l1 = create_linked_list([9, 9, 9])  # Represents 999
l2 = create_linked_list([1])        # Represents 1
result = solution.addTwoNumbers(l1, l2)
print("Test Case 3:")
print_linked_list(result)  # Expected Output: 0 -> 0 -> 0 -> 1

# Test case 4: 123 + 987 = 1110
l1 = create_linked_list([3, 2, 1])  # Represents 123
l2 = create_linked_list([7, 8, 9])  # Represents 987
result = solution.addTwoNumbers(l1, l2)
print("Test Case 4:")
print_linked_list(result)  # Expected Output: 0 -> 1 -> 1 -> 1

