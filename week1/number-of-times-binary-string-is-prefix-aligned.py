
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        max_index = 0
        curr_sum = 0
        
        for i in range(len(flips)):
            curr_sum += flips[i]
            max_index = max(max_index, flips[i])
            
            if curr_sum == (max_index * (max_index + 1)) // 2:
                count += 1
        
        return count