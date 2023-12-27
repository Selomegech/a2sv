class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ=[]
        for i in range(len(mat)):
            for j in range (len(mat)):
                if i==j or i+j == len(mat)-1:
                    
                    summ.append(mat[i][j])
            
        return sum(summ)

                    

        

        