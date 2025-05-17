class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #  to keep the track of the current row
        current = 0
        # to keep track of flipping
        going_down = False
        # declare new 2D array
        rows = [''] * numRows
        # base case
        if numRows == 1 or numRows >= len(s):
            return s
        
        for char in s:
            rows[current] += char
            
            #  check the bounds: upper and lower
            if current == 0 or current == numRows - 1:
                going_down = not going_down
            if going_down:
                current += 1
            else:
                current -= 1
        return ''.join(rows)
    
     
if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    s = "PAYPALISHIRING"
    numRows = 3
    print(solution.convert(s, numRows))
    
     # Test Case 2
    s1 = "PAYPALISHIRING"
    numRows1 = 4
    print(solution.convert(s1, numRows1))
    
    # Test Case 3
    s2 = "A"
    numRows2 = 1
    print(solution.convert(s2, numRows2))
    