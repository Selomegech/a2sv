from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        target = len(arr) // 4

        count = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                count += 1
                if count > target:
                    return arr[i]
            else:
                count = 1

        return arr[0]
        