import random

class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            # add to the map
            self.numMap[val] = len(self.numList) # index => len
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            idx = self.numMap[val] 
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = idx
            del self.numMap[val]
        return res

    def getRandom(self) -> int:
        
        return random.choice(self.numList)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

solution = RandomizedSet()
print(solution.insert(1))  # Expected: True
print(solution.remove(2))  # Expected: False
print(solution.insert(2))  # Expected: True
print(solution.getRandom())  # Expected: 1 or 2
print(solution.remove(1))  # Expected: True 