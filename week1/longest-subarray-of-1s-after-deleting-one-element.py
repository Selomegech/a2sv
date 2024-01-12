class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        i , j = 0 , 0
        chance = 1
        count = 0
        removed = True
        while j < len(nums):
            if nums[j] == 0 and chance == 0:
                j = x+1
                ans = max(ans , count)
                
                count = 0
                chance = 1
            if nums[j] == 0 and chance != 0:
                chance -= 1
                removed = False
                x = j
                
            if nums[j] == 1:
                    count += 1
                    # print(nums[j])
            j += 1
            # print(count) 
        if removed:
            ans = max ( ans , count) -1
        else :
            ans = max (ans , count )
        return ans 

        