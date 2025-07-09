
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