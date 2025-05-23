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
# def post_order(node):
#     if not node:
#         return

#     post_order(node.left)
    
#     post_order(node.right)
#     print(node)
# print(post_order(A))



# Level Order traversal bfs - time and space o(N)

from collections import deque


def level_order(node):
    q = deque()
    
    q.append(node)
    
    while q:
        node = q.popleft()
        print(node)
        if node.left:
            q.append(node.left)
            if node.right: 
                q.append(node.right)
                
print(level_order(A))
    
# check if the value exists dfs time and space o(N)

def search(node, target):
    if not node:
        return False
    
    if node.val == target:
        return True
    
    return search(node.left, target) or search(node.right, target)

print(search(A, 6))
        
    #   ----------------------------------------   
A2 = TreeNode(5)   
B2 = TreeNode(1)
C2 = TreeNode(8)
D2 = TreeNode(-1)
E2 = TreeNode(3)
F2 =TreeNode(7)
G2 = TreeNode(9)

A2.left, A2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2

print(A2)

# search in time : O(logn), spaceO(logn)
def search_bst(node, target):
    if not node: 
        return False
    
    if node.val == target:
        return True
    
    elif targt < node.val:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)
    
    print(search_bst(A2, 6))