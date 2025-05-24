
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # step 1 - base case
        if not root:
            return None
        # step 2 - inverting
        root.left, root.right = root.right, root.left
        # step 3 - recursively call the method
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
# test cases:

# ...existing code...

def print_level_order(root):
    if not root:
        print("[]")
        return
    from collections import deque
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    print(result)

solution = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
print("Original tree:")
print_level_order(root)
inverted = solution.invertTree(root)
print("Inverted tree:")
print_level_order(inverted)
# solution = Solution()
# root = TreeNode(1, TreeNode(2), TreeNode(3))
# print(solution.invertTree(root))
