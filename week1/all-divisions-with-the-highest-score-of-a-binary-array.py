from typing import List

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        numZeros = 0

        
        for i in range(len(nums)):
            numZeros += 1 if nums[i] == 0 else 0

        
        iScores = {}
        bestScore = -1
        oneRightCount = 0
        for i in range(len(nums), -1, -1):
            if i < len(nums) and nums[i] == 1:
                oneRightCount += 1
            else:
                numZeros -= 1

            score = numZeros + oneRightCount

            if score > bestScore:
                bestScore = score

            if score in iScores:
                iScores[score].append(i)
            else:
                iScores[score] = [i]

        return iScores[bestScore]