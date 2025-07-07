
from typing import List
import collections
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, WordList: List[str]) -> int:
        seen = set()
        
        # base case
        if endWord not in WordList:
            return 0
        
        def bfs(cur, step):
            wordSet = set(WordList)
            q = collections.dedque()
            
            seen.add(cur)
            q.append((cur, step))
            
            while q:
                # pop from the queue to get the current element and # of steps
                cur, steps = q.popleft()
                
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
                            return steps + 1
                        
                        # add the other case to the set and queue
                        if nei in wordSet and nei not in seen:
                            seen.add(nei)
                            q.append((nei, step))
                            
            return 0
        return bfs(beginWord, 1)
                
            