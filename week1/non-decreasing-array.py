class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        modified = False
        
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                if modified:
                    return False
                
                if i > 0 and nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]
                
                modified = True
        
        return True