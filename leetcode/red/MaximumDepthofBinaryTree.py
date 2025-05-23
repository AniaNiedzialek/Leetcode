# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	res = 0
	def maxDepth(self, root: TreeNode=None) -> int:
		self.res = 0
		self.dfsHelper(root, 1)

		return self.res


	def dfsHelper(self, cur: TreeNode, level: int=1) -> int:
		if cur == None:
			return

		self.res = max(level, self.res)
		self.dfsHelper(cur.left, level + 1)
		self.dfsHelper(cur.right, level + 1)
