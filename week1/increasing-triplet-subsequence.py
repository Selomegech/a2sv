class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        result= False
        
        maxi=[nums[len(nums)-1]] 
        mini=[nums[0]]
        for i in range (1,len(nums)):
           
            mini.append(min(nums[i],mini[-1]))
        for i in range (len(nums)-2,-1,-1):
            maxi.append(max(nums[i],maxi[-1]))
        maxi.reverse()
        
        for i in range (1,len(nums)-1):
            
            if nums[i] > mini[i-1] and nums[i]< maxi[i+1]:
                return True
        return False
        