from typing import List

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        
        for i in path + "/":
            
            # case 1 - if the character is a slash
            if i == "/":
                # subcase 1 - if the current string is not empty
                if cur == "..":
                    if stack:
                        stack.pop()
                # subcase 2 - if the current string is empty or a dot
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur =""
            # case 2 - otherwise
            else:
                cur += i
                
        return  "/" + "/".join(stack)
            
# test cases
solution = Solution()
print(solution.simplifyPath("/home/"))