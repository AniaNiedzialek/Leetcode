A = [-3, -1, 0, 1, 4, 7]


# naive way 
if -1 in A:
    print(True)
    


# traditional Binary Search - Looking up if the number is in array:
# Time: O(logn)
# space: O(1)



def binary_search(arr, target):
    N = len(arr)
    L = 0
    R = N - 1   

    while L <= R:
        # M = (L + R) // 2
        M = L + (R - L) // 2 # more efficient part
        
        # if the array:
        if arr[M] == target:
            return True
        elif arr[M]> target:
            # updated R
            R = M - 1
        else:
            #  to search in the right side
            L = M + 1
            
        


    return False


print(binary_search(A, 0))
print(binary_search(A, -10))
print(binary_search(A, 4))
print(binary_search(A, -100))

# Other technique
# Based on the condition

# [F,F, F, F, T, T, T, T]

B =[False, False, False, False, True, True, True]
def binary_search_condition(arr):
    N = len(arr)
    L =0
    R =N - 1
    while L < R:
        # we need to force it to escape at some point
        M = (L + R) // 2
        
        # check the conditions
        if B[M]:
            R = M
        else:
            L = M + 1
            
    # return L or R
    
    return L 

print(binary_search_condition(B))