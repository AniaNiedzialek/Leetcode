
from typing import Optional, List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        cur = root

        res = []
        q = collections.deque([root])
        
        
        # base case
        if not root:
            return res
      
        while q:
            
            qLen = len(q)
            
            store = []
            for i in range(qLen):
                node = q.popleft()
                store.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            total = sum(store)
            average = total/len(store)
            res.append(average)
        print(res)
        return res