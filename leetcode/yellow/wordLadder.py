
from typing import List
import collections
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seen = set()
        
        # base case
        if endWord not in wordList:
            return 0
        
        def bfs(cur, step):
            wordSet = set(wordList)
            q = collections.deque()
            
            seen.add(cur)
            q.append((cur, step))
            
            while q:
                # pop from the queue to get the current element and # of steps
                cur, step = q.popleft()
                
                # check the cur against possible letters
                for i in range(len(cur)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        
                        # check each letter against the curr[i]:
                        if c == cur[i]:
                            continue
                        # get the neighbor letter
                        nei = cur[:i] + c + cur[i + 1:]
                        
                        # check if found solution
                        if nei == endWord:
                            return step + 1
                        
                        # add the other case to the set and queue
                        if nei in wordSet and nei not in seen:
                            seen.add(nei)
                            q.append((nei, step + 1))
                            
            return 0
        return bfs(beginWord, 1)
                
            
# test cases
sol = Solution()
beginWord = 'hit'
endWord = "cog"
WordList = ["hot","dot","dog","lot","log","cog"]

print(f"Test Case 1: ", sol.ladderLength(beginWord, endWord, WordList)) # Expected: 5

beg1 = "lost"
end1 = "miss"
word = ["most","mist","miss","lost","fist","fish"]
print(f"Test Case 2: ", sol.ladderLength(beg1, end1, word)) # expected: 4