# HASHSETS


s = set()
print(s)
#
# Adding elements to the set takes on average O(1) time

s.add(1)
s.add(2)
s.add(3)
print(s)

# Lookup if the item is in the set takes on average O(1) time
if 1 in s:
    print("1 is in the set")
else:
    print("1 is not in the set")
    
if 1 not in s:
    print("1 is not in the set")

# remove an element from the set takes on average O(1) time

s.remove(1)
print(s)

string ='aaaaaaaaaaaabbbbbbbbbbccccccccceeeeeeeeeee'
sett = set(string) # will take O(S) time and only include unique characters
print(sett)


# loop htrough the elements of the set takes on average O(n) time
for i in s:
    print(i)
    


