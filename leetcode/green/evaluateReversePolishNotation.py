from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for c in tokens:
            # step 1 - write 4 cases
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second / first))

            else:
                stack.append(int(c))
        return stack.pop()
# test cases

sol = Solution()
print(sol.evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9
print(sol.evalRPN(["4", "13", "5", "/", "+"]))  # Output: 6
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # Output: 22