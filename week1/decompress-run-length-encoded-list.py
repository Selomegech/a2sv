from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed_list = []
        
        for i in range(0, len(nums), 2):
            frequency = nums[i]
            value = nums[i+1]
            decompressed_list.extend([value] * frequency)
        
        return decompressed_list