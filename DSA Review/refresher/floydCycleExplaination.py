# floyd_cycle_explanation.py

class ListNode:
    """
    Class to represent a node in a singly linked list.
    Each node has a value and a pointer to the next node.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: ListNode) -> bool:
    """
    Floyd's Cycle Detection Algorithm (Tortoise and Hare)

    Purpose:
        Detects if a cycle exists in a singly linked list.

    How it works:
        - Use two pointers: slow (moves 1 step) and fast (moves 2 steps).
        - If a cycle exists, these pointers will eventually meet inside the loop.
        - If the list ends (fast reaches None), no cycle exists.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        head (ListNode): The head of the linked list.

    Returns:
        bool: True if a cycle exists, False otherwise.
    """
    # Initialize two pointers at the head of the list
    slow = head
    fast = head

    # Traverse the list with both pointers
    while fast and fast.next:
        slow = slow.next           # Move slow by 1 step
        fast = fast.next.next      # Move fast by 2 steps

        # If the pointers meet, a cycle is detected
        if slow == fast:
            return True

    # If fast reaches the end, no cycle exists
    return False


# Sample usage for explanation purposes only (this part can be commented out in production):

if __name__ == "__main__":
    # Creating a linked list with a cycle: 3 -> 2 -> 0 -> -4 -> (points back to 2)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle

    # Run the cycle detection
    print("Cycle detected?" , hasCycle(node1))  # Output: True
