


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
	def countNodes(self, root: TreeNode=None) -> int:
		if root == None:
			return 0

		return 1 + self.countNodes(root.left) + self.countNodes(root.right)


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

    # Test case 1: Complete binary tree
    #      1
    #     / \
    #    2   3
    #   / \  /
    #  4  5 6
    root1 = TreeNode(1,
                     TreeNode(2, TreeNode(4), TreeNode(5)),
                     TreeNode(3, TreeNode(6)))
    print("Test case 1 (complete tree):", solution.countNodes(root1))  # Expected: 6

    # Test case 2: Single node
    root2 = TreeNode(1)
    print("Test case 2 (single node):", solution.countNodes(root2))  # Expected: 1

    # Test case 3: Empty tree
    root3 = None
    print("Test case 3 (empty tree):", solution.countNodes(root3))  # Expected: 0

    # Test case 4: Full tree with 7 nodes
    #      1
    #     / \
    #    2   3
    #   / \ / \
    #  4  5 6  7
    root4 = TreeNode(1,
                     TreeNode(2, TreeNode(4), TreeNode(5)),
                     TreeNode(3, TreeNode(6), TreeNode(7)))
    print("Test case 4 (full tree):", solution.countNodes(root4))  # Expected: 7