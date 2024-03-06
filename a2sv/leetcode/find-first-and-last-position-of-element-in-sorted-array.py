class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1 , -1]
        
        low = -1
        high = len(nums) -1 
        ans = [-1,-1]
        while low+1 <high:
            mid = (low + high ) // 2
            
            if nums[mid] >= target:
                high = mid
            else:
               low = mid
        ans[0] = high 
        # if nums[low] != target:
        #     return [-1 , -1]
        
        
        high = len(nums)
        while low+1 < high:
            mid = (low +high) // 2
            if nums[mid] <= target:
                low = mid
            else:
                high = mid 
        ans[1] = low
        return ans 
        



        