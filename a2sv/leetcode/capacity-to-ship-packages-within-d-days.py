class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights) 
        res = right
        def helper(mid):
            curr = mid 
            ships = 1
            for i in weights:
                if curr -i < 0:
                    ships += 1
                    curr = mid 
                    
                curr -= i
            return (ships <= days)
        while left<=right:
            mid = (left +right)//2
            if helper(mid):
                res = min(res , mid )
                right = mid-1
            else:
                left = mid +1
        return res






        