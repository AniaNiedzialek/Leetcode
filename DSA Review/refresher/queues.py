# Queues  - FIFO

from collections import deque
# deque double ended queue - has two ends,w e can add stuff to right and pop from right as well as left side - O(1)
q = deque()
print(q)

# Enqueue - add element to the right - o(1)
q.append(5)
q.append(6)
q.append(7)

print(q)

# Dequeue - removed an element from the left - O(1)
q.popleft()
print(q)

# q.pop() will treat it just as a stack

# peak from left side
q[0]
print(q[0])

q[-1]
print(q[-1])