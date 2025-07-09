


class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        col = set()
        posDiag = set()
        negDiag = set()

        def back(r):
            # base case 
            if r == n:
                nonlocal res
                res += 1
                print(res)
                return
            # otherwise
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                back(r + 1)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)


        back(0)
        return res