# Binary Trees

class TreeNode:
    # constructor
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)
    
    
A = TreeNode(1)   
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F =TreeNode(10)


A.left = B
A.right = C
B.left = D
B.right = E 
C.left  = F 


# treat the root as the tree now
# print(A)


# Recursive pre order traversal DFS time O(N), space O(N)
def pre_order(node):
    if not node:
        return
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)
    
    
# print(pre_order(A))
    
    
    # In order traversal 
# def in_order(node):
#     if not node:
#         return


#     in_order(node.left)
#     print(node)
#     in_order(node.right)

# print(in_order(A))

# Post order traversal
def post_order(node):
    if not node:
        return

    post_order(node.left)
    
    post_order(node.right)
    print(node)
print(post_order(A))

