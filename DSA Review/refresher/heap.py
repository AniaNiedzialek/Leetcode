# build a min heap - heapify
# time: O(n), space: O(1)

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
# to satisfy the heap property, we need to rearrange the elements
import heapq
heapq.heapify(A)
print("Heapified array:", A)

# main opearation - heap push
# time: O(log n)

heapq.heappush(A, 4)
# A is a heap- insert


# heap pop
# time O(log n)

minn = heapq.heappop(A)
print("Popped minimum element:", minn)
print("Array after popping minimum:", A)

# heap sort - sorts the array in place by popping all elements
# time: O(n log n), space: O(n) but we can do it in O(1) space

def heapsort(arr):
    heapq.heapify(arr)
     #rearrange the array 
    n = len(arr)
    new_list = [0] * n
     
    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i]  = minn
    return new_list

A = ([1,3,5,7,9,2,4,6,8,0])
print("Sorted array using heap sort:", heapsort(A))

# heap push pop: time: O(log n), space: O(1)
# heapq.heappushpop(A,99)
A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

print(heapq.heappushpop(A,99))

# for max heap you need to invert the values
# A = [-x for x in A]  # invert the values