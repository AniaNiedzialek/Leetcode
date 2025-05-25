from typing import List
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # step 1 - base case
        if not inorder or not postorder:
            return None
        # step 2 -  find root
        value = postorder.pop()
        root = TreeNode(value)
        # step 3 - find root in inorder
        mid = inorder.index(value)
        # step 4 - recursively build the tree
        root.right = self.buildTree(inorder[mid + 1:], postorder)
        root.left = self.buildTree(inorder[:mid], postorder)
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
    inorder1 = [9,3,15,20,7]
    postorder1 = [9,15,7,20,3]
    root1 = solution.buildTree(inorder1, postorder1)
    print("Test case 1 (level order):")
    print_level_order(root1)  # Expected: [3, 9, 20, None, None, 15, 7]

    # Test case 2: Single node
    inorder2 = [1]
    postorder2 = [1]
    root2 = solution.buildTree(inorder2, postorder2)
    print("Test case 2 (single node):")
    print_level_order(root2)  # Expected: [1]

    # Test case 3: Empty tree
    inorder3 = []
    postorder3 = []
    root3 = solution.buildTree(inorder3, postorder3)
    print("Test case 3 (empty tree):")
    print_level_order(root3)  # Expected: []