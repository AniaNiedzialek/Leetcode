A = [1, 2, 3]

print(A)

# Append - insert element at the end of the array - on average O(1)
A.append(4)
print(A)

# Pop - deleting the element at the end of the array - on average O(1)
A.pop()
print(A)

# Insert - insert element not at the end of the array - O(n)
A.insert(0, 0) # need the position to insert
print(A)

# Modify - change the value of an element in the array - O(1)
A[0] = 10
print(A)

# Accessing - get the value of an element in the array - O(1)
print(A[0])

# if the element exists
if 6 in A:
    print("6 is in A")
elif 1 in A:
    print("1 is in A")