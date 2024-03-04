
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(nums, path):
            if len(path) == len(nums):
                ans.append(path[:])
            
            for i in nums:
                if i not in path:
                    path.append(i)
                    backtrack(nums , path)
                    path.pop()
        backtrack(nums , path)
        return ans 