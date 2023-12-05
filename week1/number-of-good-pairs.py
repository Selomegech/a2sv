from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        freq = {}
        
        # Count the frequencies of each number
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Calculate the number of good pairs
        for num in freq:
            count += (freq[num] * (freq[num] - 1)) // 2
        
        return count