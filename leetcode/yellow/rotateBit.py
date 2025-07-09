class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # logic and
            bit = (n >> i) & 1
            # logic or 
            res = res | (bit << (31 - i))
        return res
    
# ...existing code...

if __name__ == "__main__":
    solution = Solution()
    # Test case 1: Example from LeetCode
    n1 = int('00000010100101000001111010011100', 2)
    print(solution.reverseBits(n1))  # Expected: 964176192 (which is 00111001011110000010100101000000 in binary)

    # Test case 2: All bits set
    n2 = 0xFFFFFFFF
    print(solution.reverseBits(n2))  # Expected: 0xFFFFFFFF (4294967295)

    # Test case 3: Only the lowest bit set
    n3 = 1
    print(solution.reverseBits(n3))  # Expected: 2147483648 (which is 10000000000000000000000000000000 in binary)

    # Test case 4: Only the highest bit set
    n4 = 0x80000000
    print(solution.reverseBits(n4))  # Expected: 1

    # Test case 5: Zero
    n5 = 0
    print(solution.reverseBits(n5))  # Expected: 0