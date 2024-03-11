class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        left = max(nums) 
        right = sum(nums)

        def helper(mid):
            count = 0
            summ = 0
            for i in nums:
                summ += i
                if summ > mid:
                    count += 1
                    summ = i
            count += 1 
            if count <= k:
                return(True)

        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        return left


                
                
                
