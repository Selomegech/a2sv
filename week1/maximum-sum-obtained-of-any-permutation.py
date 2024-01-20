class Solution:
    def maxSumRangeQuery(self, nums, requests):
        n = len(nums)
        freq = [0] * (n + 1)

        for start, end in requests:
            freq[start] += 1
            freq[end + 1] -= 1

        for i in range(1, n + 1):
            freq[i] += freq[i - 1]

        nums.sort(reverse=True)
        freq.sort(reverse=True)

        maxSum = 0
        modulo = 10**9 + 7

        for i in range(n):
            maxSum = (maxSum + nums[i] * freq[i]) % modulo

        return maxSum