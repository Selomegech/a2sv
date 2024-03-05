class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        path = []
        def helper(num,target):
            if target == 0  :
                ans.append(path[:])
                return
            if target <0:
                return
                
            for i in range(num,len(candidates)):
                if i > num and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
        
                helper(i+1, target-candidates[i])

                path.pop()
        ans=[]

        helper(0,target)
        return ans 

        