class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        m = max(nums)
        summ = 0
        ans = 0
        for i in range(len(nums)):
            summ += nums[i]
            average = summ /(i+1)
            ceiling_value = math.ceil(average)
            ans = max(ans , ceiling_value)
        return ans 

            
        