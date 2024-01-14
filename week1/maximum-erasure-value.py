from collections import defaultdict

class Solution:
    def maximumUniqueSubarray(self, nums):
        score = 0
        i = 0
        j = 0
        summ = 0
        hold = defaultdict(int)  
        
        while j < len(nums):
            if nums[j] not in hold or hold[nums[j]] < i:
                hold[nums[j]] = j
                summ += nums[j]
                j += 1
            else:
                i = hold[nums[j]] + 1
                hold[nums[j]] = j
                summ = sum(nums[i:j+1])  
                j += 1

            score = max(score, summ)
        
        return score