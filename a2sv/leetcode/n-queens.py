class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        matrix = [['.'] * n for i in range(n)]
        pos_diagonal = set()
        neg_diagonal = set()
        cols = set()
        ans = [] 
        def backtrack(r):
            if r==n:
                ans.append([''.join(r) for r in matrix])
            for c in range(n):
                if c in cols or (r+c) in pos_diagonal or (r-c) in neg_diagonal:
                    continue
                cols.add(c)
                neg_diagonal.add(r-c)
                pos_diagonal.add(r+c)
                matrix[r][c] = 'Q'
                backtrack(r+1)
                cols.remove(c)
                neg_diagonal.remove(r-c)
                pos_diagonal.remove(r+c)
                matrix[r][c] = '.'
        backtrack(0)
        return ans 


            