class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dicti= {}
        for i in range(len(nums) ):
            dicti[nums[i]]= i 
        for num, value in operations:
            if num in dicti:
                r = dicti[num]
                nums[r] = value
                
                # dicti.pop(num)
                dicti[value] = r
              
                    
                    
            
        return nums
        