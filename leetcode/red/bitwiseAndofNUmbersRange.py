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