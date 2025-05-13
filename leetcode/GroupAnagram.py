from collections import defaultdict
from typing import List  # Import List from typing

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagram_map[key].append(word)

        return list(anagram_map.values())

# Test case
solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution.groupAnagrams(strs))