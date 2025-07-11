from typing import List

class Solution:
    def calcualte(self, s: str) -> int:
        stack = []
        cur = res = 0
        sign = 1
        
        for c in s:
            # case 1 - if the character is a digit
            if c.isdigit():
                cur = cur * 10 + int(c)
            # case 2 - if the character is a sign
            elif c == "+" or c == "-":
                res += sign * cur
                sign = 1 if c == "+" else -1
                cur = 0
            # case 3 - if the character is an open parenthesis
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif c == ")":
                res += sign * cur
                res *= stack.pop()
                res += stack.pop()
                cur = 0
        return res + sign * cur
# test cases
solution = Solution()
print(solution.calcualte("1 + 1"))  # Output: 2
print(solution.calcualte(" 2-1 + 2 "))  # Output: 3
print(solution.calcualte("(1+(4+5+2)-3)+(6+8)"))  # Output: 23
print(solution.calcualte("2-(5-6)"))  # Output: 3           
                

