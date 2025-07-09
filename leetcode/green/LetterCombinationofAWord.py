from typing import List

class Solution():
    def letterCombinations(self, digits:str) -> List[str]:
        # declare the result array to return
        res = []
        # create the mapping
        digitMap = {
             "2" : "abc",
            "3" :  "def",
            "4" : "ghi",
            "5" : "jkl", 
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        # define the backtracking function
        def back(i, curStr):
            # base case - if passed
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            # otherwise keep checking recursively
            for c in digitMap[digits[i]]:
                back(i + 1, curStr + c)
                
        # call the function
        if digits:
            back(0, "")
            
        return res
        
# test cases
sol = Solution()
digits = "23"
print("Test Case 1: ", sol.letterCombinations(digits))

# 2
digits2 = "9"
print("Test Case 2: ", sol.letterCombinations(digits2) )

# 3 
digits3 = ""
print("Test Case 3: ", sol.letterCombinations(digits3))