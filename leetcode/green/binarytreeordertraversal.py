

from typing import Optional, List
import collections
class TreeNode:
    def __init__ (self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        

class Solution:
    def levelOrder(self, root:Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque([root]) 
        
        # base case
        if not root:
            return res
        
        while q:
            store = []
            for i in range(len(q)):
                node = q.popleft()
                store.append(node.val)
                if node.left:
                    q.append(node.left) 
                if node.right:
                    q.append(node.right)
            res.append(store)
        return res