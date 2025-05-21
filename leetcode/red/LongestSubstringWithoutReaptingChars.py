class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # print(f"s is {s}, {s[0]}")
        size = len(s)
        temp = []
        max_count = 0
        count = len(temp)

        if not s:
            return 0

        for c in s:
            if c in temp:
                while c in temp:
                    removed = temp.pop(0)
                
            
            temp.append(c)
            max_count = max(max_count, len(temp))
                
      
        return max_count


    