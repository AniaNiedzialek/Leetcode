class Solution:
    def kthSmallest(self, root, k: int) -> int:
        val = []
        
        # inorder traversal
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            val.append(root.val)
            inorder(root.right)
            
        inorder(root)
        for i in range(len(val)):
            return val[k-1]