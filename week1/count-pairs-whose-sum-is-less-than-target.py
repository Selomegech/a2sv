class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        
        
        count = 0
        for i in range (len(nums)):
            j = 1
            while j < len(nums):
                if nums[i] + nums[j] < target and i < j:
                    # print([i , j ])
                    count += 1
                j+=1

        return count 
        