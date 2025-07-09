class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n  >> 1
        return res
    
    # ...existing code...

if __name__ == "__main__":
    solution = Solution()
    # Test case 1: 11 (binary 1011) has 3 ones
    print(solution.hammingWeight(11))  # Expected: 3

    # Test case 2: 128 (binary 10000000) has 1 one
    print(solution.hammingWeight(128))  # Expected: 1

    # Test case 3: 0 has 0 ones
    print(solution.hammingWeight(0))  # Expected: 0

    # Test case 4: 4294967295 (all 32 bits set)
    print(solution.hammingWeight(0xFFFFFFFF))  # Expected: 32