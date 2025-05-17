# Valid Anagram
# Solved 
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}
        count = 0

        for i in s:
            print(f" i is {i}")
            if i not in mapS:
                mapS[i] = 0
                # print(f"maps: {mapS}")
            mapS[i] += 1
        for i in t:
            if i not in mapT:
                mapT[i] = 0
            mapT[i] += 1
            # print(f"now maps: {mapS}, mapT = {mapT}")

        return mapS == mapT
    
solution  = Solution()
string = "racecar"
string2 = "carrace"
print(solution.isAnagram(string, string2))  # Output: True