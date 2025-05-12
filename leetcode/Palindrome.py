class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        temp = ""
        temp2 = ""

        for c in s:
            if c.isalnum():
                temp += c
        for c in temp:
            temp2 += c.lower()
        size = len(temp2)
        i = 0
        j = size - 1

        while j < size and i < size - 1:
            if temp2[i] == temp2[j]:
                i += 1
                j -= 1
                
                
            else:
                return False


        return True

# to run:
solution = Solution()
