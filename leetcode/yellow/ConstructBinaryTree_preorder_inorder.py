
from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # step 1 - base case
        if not preorder or not inorder:
            return None
        # step 2 - find the root
        root = TreeNode(preorder[0])
        # step 3 - find the root in the the inorder
        mid = inorder.index(preorder[0])
        # step 4 - recursively build tree
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

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
    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
    print(result)

if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example tree
    preorder1 = [3,9,20,15,7]
    inorder1 = [9,3,15,20,7]
    root1 = solution.buildTree(preorder1, inorder1)
    print("Test case 1 (level order):")
    print_level_order(root1)  # Expected: [3, 9, 20, None, None, 15, 7]

    # Test case 2: Single node
    preorder2 = [1]
    inorder2 = [1]
    root2 = solution.buildTree(preorder2, inorder2)
    print("Test case 2 (single node):")
    print_level_order(root2)  # Expected: [1]

    # Test case 3: Empty tree
    preorder3 = []
    inorder3 = []
    root3 = solution.buildTree(preorder3, inorder3)
    print("Test case 3 (empty tree):")
    print_level_order(root3)  # Expected: []