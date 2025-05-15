# Hashmaps - Dictionaries
d = {'greg':1, 'john':2, 'jane':3}
print(d)

# add a key:val pair in O(1) time:
d['arsh'] = 4
print(d)

# check for presence of a key in O(1) time:
if 'greg' in d:
    print("greg is in the dictionary")
else:
    print("greg is not in the dictionary")
    
    # check the value corresponding to the key
print(d['greg']) # assuming key is present
# if key is not present, it will throw a KeyError

# loop over key:val pairs in O(n) time
for key,val in d.items():
    print(key, val)
    
# Defaultdict
from collections import defaultdict
d = defaultdict(int) # default value is 0defaultdict(int)
print(d)

d[2]

# Counter - maybe not ideal for an interview, but useful
from collections import Counter
string = 'aaaaaaabbbcccccc'
# count the frequency of each character in the string
counter = Counter(string)
print(counter)
