class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentsum = sum(nums[:k])
        maxsum= currentsum
        for i in range(k,len(nums)):
            currentsum += nums[i]- nums[i-k]
            maxsum= max(maxsum, currentsum)
        return maxsum/k

        