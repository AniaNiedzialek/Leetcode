from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS - check if same structure and same values

        def balances(p,q):
            # step 1 - base case
            if not p and not q: # both are invalid entries
                return True
            # step 2 - if either is invalid
            if (not p and q) or (p and not q):
                return False
            # step 3 - check if different values
            if p.val != q.val:
                return False
            return balances(p.left, q.left) and balances(p.right, q.right)
        
        return balances(p, q)
    
    
    
solution = Solution()

# Test case 1: Both trees are empty
p1 = None
q1 = None
print("Test case 1 (both empty):", solution.isSameTree(p1, q1))  # Expected: True

# Test case 2: Both trees have one node, same value
p2 = TreeNode(1)
q2 = TreeNode(1)
print("Test case 2 (single node, same value):", solution.isSameTree(p2, q2))  # Expected: True

# Test case 3: Both trees have one node, different value
p3 = TreeNode(1)
q3 = TreeNode(2)
print("Test case 3 (single node, different value):", solution.isSameTree(p3, q3))  # Expected: False

# Test case 4: Trees with same structure and values
#    1
#   / \
#  2   3
p4 = TreeNode(1, TreeNode(2), TreeNode(3))
q4 = TreeNode(1, TreeNode(2), TreeNode(3))
print("Test case 4 (same structure and values):", solution.isSameTree(p4, q4))  # Expected: True

# Test case 5: Trees with different structure

#    4
#   / \
#  4   5
# /
#6
p5 = TreeNode(4, TreeNode(4), TreeNode(5))
q5 = TreeNode(4, TreeNode(4, TreeNode(5)), TreeNode(6))
print("Test case 4 (same structure and values):", solution.isSameTree(p5, q5))  # Expected: False
