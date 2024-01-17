class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range (len(nums)):
            leftsum = sum(nums[:i])
            rightsum = sum(nums[i+1:])
            if leftsum == rightsum:
                return i
        return -1

        