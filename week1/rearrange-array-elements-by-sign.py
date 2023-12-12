class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative=[num for num in nums if num<0]
        positive=[numm for numm in nums if numm>0]
        result=[]

        for i in range (len(negative)):
            
                result.append(positive[i])
                result.append(negative[i])
            


            
        return result

        
        