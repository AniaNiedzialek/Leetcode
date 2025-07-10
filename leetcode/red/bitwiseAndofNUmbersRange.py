class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0

        for i in range(32):
            bit = (left >> i) & 1 # zero out eveyr bit except the rightmost bit
            if not bit:
                continue
            
            remainder = left % (1 << (i + 1))
            dif = (1 << (i + 1 )) - remainder
            if right - left < dif:
                res = res |(1 << i)




        return res
    
# test cases
# ...existing code...

if __name__ == "__main__":
    solution = Solution()
    # Test case 1: Range with common prefix
    print(solution.rangeBitwiseAnd(5, 7))  # Expected: 4

    # Test case 2: Range with no common bits
    print(solution.rangeBitwiseAnd(0, 1))  # Expected: 0

    # Test case 3: Single number
    print(solution.rangeBitwiseAnd(3, 3))  # Expected: 3

    # Test case 4: Large range
    print(solution.rangeBitwiseAnd(1, 2147483647))  # Expected: 0

    # Test case 5: Range with all bits set
    print(solution.rangeBitwiseAnd(7, 15))  # Expected: 0