class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        nums.sort(reverse = True)
        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1
            while left < right :
                if nums[left] + nums[right] > nums[i]:
                    
                    ans += right-left
                    left += 1
                else:
                    right -= 1
        return ans 
                
             
                
                
            

        