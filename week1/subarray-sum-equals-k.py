class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        dictionary = defaultdict(int)
        dictionary[0] = 1
        count  = 0
        for i in range (len(nums)):
            sum += nums[i]
            if sum-k in dictionary:
                count += dictionary[sum-k]
            dictionary[sum] += 1
        return count  