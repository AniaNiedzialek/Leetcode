# append to the end of the string - O(n)
s = 'hello'

b = s + ' z'
print(b)  # hello z

# strings in python are immutable!  
# check if something is in the string
if 'h' in s:
    print("h is in s")
# check if something is not in the string
if 'z' not in s:
    print("z is not in s")
# check if something is in the string
if 'hello' in s:
    print("hello is in s")
# check if something is not in the string
if 'hello' not in s:
    print("hello is not in s")


# Access different positions in the string
print(s[0])  # h
print(s[1])  # e
print(s[2])  # l
print(s[3])  # l
print(s[4])  # o

# check the length of the string - O(1)
print(len(s))  # 5