from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # pointer for overwriting elements
        j = 0  # pointer for iterating through the array

        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i