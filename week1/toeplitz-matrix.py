class Solution:
    def isToeplitzMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])

        # Iterate over each element except the first row and first column
        for i in range(1, m):
            for j in range(1, n):
                # Compare with the top-left element (previous diagonal element)
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False

        return True