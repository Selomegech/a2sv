from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        n = len(nums)
        threshold = n // 3

        result = [num for num in counter if counter[num] > threshold]
        return result
        