class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = -1
        right = len(matrix) -1
        def helper(mid):
            if matrix[mid][-1] < target:
                return False
            return True
        while left + 1 < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid
        x = set(matrix[right]) 
        if target in x:
            return True
        return False