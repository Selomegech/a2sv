class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        n = len(citations)
        left = 0
        right = n

        def helper(mid):
            for i in range(0 , mid):
                if citations[i] < mid:
                    return False
            return True
        
        while left <= right:
            mid = (left+right) // 2
            if helper(mid):
                left = mid+1
            else:
                right = mid-1
        
        return right


        