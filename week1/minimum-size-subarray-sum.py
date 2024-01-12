
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        windowSum = 0
        minLength = float('inf')

        while right < len(nums):
            windowSum += nums[right]

            while windowSum >= target:
                minLength = min(minLength, right - left + 1)
                windowSum -= nums[left]
                left += 1
            right += 1

        return minLength if minLength != float('inf') else 0
        
        