class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return ([1] * (rowIndex +1))
        if rowIndex == 1:
            return ([1] * (rowIndex +1))
        ans1 = self.getRow(rowIndex -1 )
        ans = [1]
        for i in range(len(ans1) - 1):
            ans .append( ans1[i] + ans1[i + 1])
        ans.append(1)
        return ans 
        
        