class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # logiic and
            bit = (n >> i) & 1
            # logic or 
            res = res | (bit << (31 - i))
        return res