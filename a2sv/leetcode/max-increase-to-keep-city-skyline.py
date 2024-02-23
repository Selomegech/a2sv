class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows_maximum = []
        col_maximum = []
        rowmax = 0
        colmax = 0

        for i in range(len(grid)):
            colmax = 0
            for j in range(len(grid)):
                colmax = max(colmax , grid[i][j])
            col_maximum.append(colmax)
        for i in range (len(grid)):
            rowmax = 0
            for j in range(len(grid)):
                rowmax = max(rowmax , grid[j][i])
            rows_maximum.append(rowmax)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                ans += abs(grid[i][j] - min(rows_maximum[j] ,col_maximum[i]))
                # print(min(rows_maximum[j] ,col_maximum[i]))
        return ans 
        
        # print(rows_maximum)
        # print(col_maximum)
        # return 0
        
            

        
        