
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def back(openN, closedN):
            # base case
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                back(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                back(openN, closedN + 1)
                stack.pop()

        back(0, 0)
        return res
    
    
# test cases:
sol = Solution()
n = 3
print(f"Test Case 1 ", sol.generateParenthesis(n))

n1 = 1
print(f"Test Case 2: ", sol.generateParenthesis(n1))