class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        pooped = False
        for i in range(len(nums)-1 , -1 , -1):
            while stack and nums[i] > stack[-1]:
                pooped = True
                x = stack.pop()
            if stack and pooped and x > nums[i]  :
                return True 
            stack.append(nums[i])
                
                    
                
        return False 

            
        
        