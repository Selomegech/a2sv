class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)
        ans = 0

        left = 0
        right = n - 1

        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ans += pow(2, right - left, mod)
                ans %= mod 
                left += 1

        return ans
             
