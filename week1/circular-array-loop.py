class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        

        for i in range(len(nums)):
            seen = set()
            pos = nums[i] > 0 
            j = i
            count = 0
            prev = i
            while True:
                sign =  nums[j]>0
                if pos == sign and j not in seen:
                    seen.add(j)
                    prev = j
                    j = (j + nums[j]) % len(nums)
                elif pos != sign:
                    break
                elif pos == sign and j in seen :
                    if prev == j:
                        break
                    return True
                count += 1
        return False 


            


            
        