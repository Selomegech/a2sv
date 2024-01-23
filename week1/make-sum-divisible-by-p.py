class Solution:
    def minSubarray(self, nums, p):
        total_sum = sum(nums)
        target_remainder = total_sum % p
        
        if target_remainder == 0:
            return 0
        
        remainders = {0: -1}
        current_remainder = 0
        min_length = len(nums)
        
        for i in range(len(nums)):
            current_remainder = (current_remainder + nums[i]) % p
            complement_remainder = (current_remainder - target_remainder) % p
            if complement_remainder in remainders:
                min_length = min(min_length, i - remainders[complement_remainder])
            remainders[current_remainder] = i
        
        if min_length == len(nums):
            return -1
        else:
            return min_length