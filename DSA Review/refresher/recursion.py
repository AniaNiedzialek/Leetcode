# Fibonacci
# F(0) = 0
# F(1) = 1
# n > 1: F(n) = F(n-1) + F(N-2)

# def F(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return F(n - 1) + F(n - 2)

# print(F(5))



# Singly linked list:
class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return str(self.val)
    

Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

print(Head)
    
# Linkedlists are recursive
def reverse(node, result=None):
    if result is None:
        result = []
    if not node:
        return result
    reverse(node.next, result)
    result.append(str(node.val))
    return result

reversed_values = reverse(Head)
print(" -> ".join(reversed_values))  # Output: 7 -> 4 -> 3 -> 1
    