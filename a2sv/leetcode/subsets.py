class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []

        def subset(nums , i):

            ans.append(path[:])

            for j in range(i, len(nums)):
                path.append(nums[j])
                subset(nums , j+1)
                path.pop()
        subset(nums , 0)
        return(ans)

        