# Singly Linked Lists and Doubly Linked Lists
# Singly Linked List

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

# to join them together
Head.next = A
A.next = B
B.next = C

print(Head) # 1 

# traverse the list - O(n)  
curr = Head
while curr: # until the curr reaches None
    print(curr)
    curr = curr.next # here we can access the next node, and eventually reach None
    
    
# Display the linked list - O(n)
def display(head):
    curr = head 
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(elements))
    # join - given a list of strings ['a', 'b', 'c'], join moves them to a single string of 'abc'
# display(Head)  # 1 -> 3 -> 4 -> 7

# search for node value - O(n)
def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
        
    return False

print(search(Head, 2))  # Output: False
print(search(Head, 3))  # Output: <SinglyNode object at ...> (node with value 3)
print(search(Head, 7))  # Output: <SinglyNode object at ...> (node with value 7)
print(search(Head, 1))  # Output: <SinglyNode object at ...> (node with value 1)
print(search(Head, 8))  # Output: False


# DOUBLY LINKED LISTS

class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.val)
    

head = tail = DoublyNode(1)
print(head)
print(tail)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
        
    print(" <-> ".join(elements))  
display(head) 

# Insert at the beginning - O(1)
def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail

head, tail = insert_at_beginning(head, tail, 3)
display(head)
    
    
# insert at the end in a doubly linked list - O(1)
def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 7)
display(head)
    