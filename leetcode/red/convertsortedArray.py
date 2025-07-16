from typing import List
import collections
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
         

        #  helper function
        def helper(l, r):
            if l > r:
                return None
            
            # recursive call
            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)

            return root
        return helper(0,len(nums) - 1)
    
    # ...existing code...

def preorder_traversal(root):
    """Helper function to print the tree in preorder (root, left, right)"""
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Odd number of elements
    nums1 = [-10, -3, 0, 5, 9]
    root1 = solution.sortedArrayToBST(nums1)
    print("Preorder traversal (test 1):", preorder_traversal(root1))
    # Expected: [0, -10, -3, 5, 9] or any valid BST preorder

    # Test case 2: Even number of elements
    nums2 = [1, 2, 3, 4]
    root2 = solution.sortedArrayToBST(nums2)
    print("Preorder traversal (test 2):", preorder_traversal(root2))
    # Expected: [2, 1, 3, 4] or [3, 1, 2, 4] (any valid BST preorder)

    # Test case 3: Single element
    nums3 = [1]
    root3 = solution.sortedArrayToBST(nums3)
    print("Preorder traversal (test 3):", preorder_traversal(root3))
    # Expected: [1]

    # Test case 4: Empty array
    nums4 = []
    root4 = solution.sortedArrayToBST(nums4)
    print("Preorder traversal (test 4):", preorder_traversal(root4))
    # Expected: []