class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum = 0
        di = defaultdict(int)
        di[0] = 1
        count = 0
        for i in range (len(nums)):
            sum += nums[i]
            if sum%k in di:
                count += di[sum%k]
            di[sum%k] += 1
        return count


        