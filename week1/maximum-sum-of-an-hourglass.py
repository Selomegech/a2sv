class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans=0
        for i in range(0,len(grid)-2):
            for j in range(0,len(grid[0])-2):
                summ = grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]
                
                ans=max(ans,summ)
        return ans