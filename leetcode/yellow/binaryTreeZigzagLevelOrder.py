from typing import Optional, List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque([root])
        left = True

        # base case
        if not root:
            return res
        
        while q:
            store = []
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                store.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not left:
                store.reverse()
            left = not left

            res.append(store)
        return res
    
 
 # ...existing code...

if __name__ == "__main__":
    # Example tree:
    #     1
    #    / \
    #   2   3
    #  / \   \
    # 4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(6))

    solution = Solution()
    print("Zigzag Level Order Traversal:")
    print(solution.zigzagLevelOrder(root))  # Expected: [[1], [3, 2], [4, 5, 6]]   