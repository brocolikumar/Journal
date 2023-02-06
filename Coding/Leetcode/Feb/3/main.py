class Solution:
    def convert(self, s: str, rows: int) -> str:
        import math
        if rows==1:
            return s
        
        sections = math.ceil( len(s)/(2*rows-2) )

        cols =  sections*(rows-1)
        
        matrix = [ [0]*cols for _ in range(rows) ]

        up = False
        row, col = 0 , 0

        for ind, val in enumerate(s):
            matrix[row][col] = val
            
            if row==rows-1 and up==False:
                up = True
                col +=1
                row -=1
                continue
            elif row==0 and up==True:
                up = False
                row += 1
                continue
            elif up==False:
                row += 1
                continue
            elif up ==True:
                row -=1
                col +=1
                continue

        
        r , c = len(matrix), len(matrix[0])
        res = ""

        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    continue
                res += matrix[i][j]

        return res
        

    

s = Solution()
string = "PAYPALISHIRING"
numRows = 4
res = s.convert(string,numRows)
print(f"This is the result: {res}")