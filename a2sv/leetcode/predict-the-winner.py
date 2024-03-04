class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        score = 0
        def helper( nums ,l , r  , flag):
            nonlocal score 
            if flag :
                if l == r:
                    return nums[l]
                
                left =  helper(nums , l+1 , r , not flag) + nums[l]
                
                right= helper(nums , l , r-1 , not flag) + nums[r]

                return (max(left , right))

            else:
                if l == r:
                    return  - nums[l]
                left = helper(nums , l+1 , r , not flag) - nums[l]
                right = helper(nums , l , r-1 ,not flag ) - nums[r]
                return (min(left , right))
            
        res = helper(nums , 0 , len(nums)-1 , True) 
        if res >= 0:
            return True
        else:
            return False

            
                


                
            
           
        return(helper(nums , 0 , len(nums)-1 , 0 , 0 , True))


        