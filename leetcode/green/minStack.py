from typing import List

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        # case 1 
        self.stack.append(val)
        # case 2
        # find val first
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]   
    def getMin(self) -> int:
        return self.minStack[-1]
    
# test cases
test = MinStack()
test.push(-2)
test.push(0)                
test.push(-3)
print(test.getMin())  # Returns -3