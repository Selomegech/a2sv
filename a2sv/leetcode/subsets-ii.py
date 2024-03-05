class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []
        def subset(num):
            if num == len(nums):
                return 
            if path not in ans:
                ans.append(path[:]) 
            for i in range(num , len(nums)):
                path.append(nums[i])
                if path not in ans:
                    ans.append(path[:]) 
                subset(i+1)
                path.pop()
        subset(0)
        return ans 
