class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 0
        right = max(nums)

        def helper(mid):
            ans = 0
            for i in nums:
                x = i
                ans += ceil(i/mid)
            return( ans <= threshold)
        while (left + 1) < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid 
        return right

        