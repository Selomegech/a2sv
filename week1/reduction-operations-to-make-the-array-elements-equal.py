from typing import List

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)  # Sort the array in descending order
        operations = 0
        n = len(nums)
        i = 1
        
        while i < n:
            if nums[i] < nums[i-1]:
                operations += i
            i += 1
        
        return operations