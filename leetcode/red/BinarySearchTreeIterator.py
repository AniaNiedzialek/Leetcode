from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left 

    def next(self) -> int:
        res = self.stack.pop()

        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left

        return res.val

    def hasNext(self) -> bool:
         return self.stack != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# ...existing code...

if __name__ == "__main__":
    # Helper to build a BST
    def build_bst():
        #      7
        #     / \
        #    3   15
        #        / \
        #       9  20
        root = TreeNode(7)
        root.left = TreeNode(3)
        root.right = TreeNode(15, TreeNode(9), TreeNode(20))
        return root

    root = build_bst()
    iterator = BSTIterator(root)

    print("Test case 1 (inorder traversal):")
    results = []
    while iterator.hasNext():
        results.append(iterator.next())
    print(results)  # Expected: [3, 7, 9, 15, 20]

    # Test case 2: Single node
    root2 = TreeNode(1)
    iterator2 = BSTIterator(root2)
    print("Test case 2 (single node):")
    print([iterator2.next() for _ in range(1) if iterator2.hasNext()])  # Expected: [1]

    # Test case 3: Empty tree
    iterator3 = BSTIterator(None)
    print("Test case 3 (empty tree):")
    print(iterator3.hasNext())  # Expected: False