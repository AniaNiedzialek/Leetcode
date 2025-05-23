# Stacks
stk = []
print(stk)

# adding new elements - O(1)
stk.append(5)
stk.append(4)
stk.append(3)

print(stk)

# removing - pop  - O(1)
# keep track of what was popped
x = stk.pop()
print(x)
print(stk)

# ask what's on top of stack - O(1)
print(stk[-1])

# ask if something is in the stack - O(1)
if stk:
    print(True)