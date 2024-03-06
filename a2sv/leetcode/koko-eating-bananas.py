class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)
        res = right

        def helper(mid):
            curr = mid
            count = 0
            arr = piles
            for i in piles:
                
                count += ceil(i/curr)

            return((h - count) >= 0)

        while (left + 1) < right:
            mid = (left+right) // 2
            if helper(mid):
                
                res = min(res , mid)
                right = mid
            else:
                left = mid
        return res 
             


        