class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)-2
        goal = len(nums)-1
        for i in range (n , -1 , -1):
            if nums[i] +i  >= goal:
                goal = i
        return (goal==0)
            




        