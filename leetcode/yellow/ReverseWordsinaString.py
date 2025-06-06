from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        # print(f"{s}, {s[0]}")
        # split the chars into separate entries
        arr = s.split()
        # print(arr)

        reverse = list(reversed(arr))

        # print(reverse)
        return ' '.join(reverse)

# All combined in one return line
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return ' '.join(s.split()[::-1])



solution = Solution()
s = "the sky is blue"
print(f"Reversed words are: ", solution.reverseWords(s))

s = "   hello world   "
print(f"Reversed words are: ", solution.reverseWords(s))

s ="    Ania: 'hi, i solved another Leetcode question !   "
print(f"Reversed words are: ", solution.reverseWords(s))