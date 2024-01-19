class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0 
        maps = { 0 : 1}
        sum = 0

        for num in nums :
            sum += num

            if sum - goal in maps:
                count += maps[sum - goal]
            if sum in maps :
                maps[sum] += 1
            else:
                maps[sum] = 1

        return count