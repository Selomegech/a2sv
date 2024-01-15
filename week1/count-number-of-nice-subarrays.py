from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + (num % 2))

        count = 0
        prefix_count = [0] * len(prefix_sums)

        for prefix_sum in prefix_sums:
            if prefix_sum >= k:
                count += prefix_count[prefix_sum - k]
            prefix_count[prefix_sum] += 1

        return count