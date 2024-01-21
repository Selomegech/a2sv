class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]

        n = len (nums)

        for i in range (1 , n):
            prefix.append(nums[i] + prefix[i-1])
        
        result = []

        for i in range(n):
            left = prefix[i]
            right = prefix[-1] - prefix[i]

            ans =  (nums[i] * (i+1) - left) + right - nums[i] * (n-i-1)

            result.append(ans)
        return result 
