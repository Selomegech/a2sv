class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path =[]
        def helper(num,target):
            if target == 0 :
                ans.append(path[:])
                return
            if target < 0:
                return
               
                
            for i in range(num,len(candidates)):
                
                path.append(candidates[i])
        
                helper(i,target-candidates[i])

                path.pop()
            

        ans=[]
        helper(0 , target)
        return ans