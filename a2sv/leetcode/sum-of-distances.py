class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        right = [0] * len(nums)
        left = [] 
        for i in range(len(nums)):
            if nums[i] not in d:
                left.append(0)
                d[nums[i]] = [1 , i]
            else:
                x = d[nums[i]][0] * abs(i - d[nums[i]][1])  + left[d[nums[i]][1]]
                left.append(x)
                d[nums[i]][0]+= 1
                d[nums[i]][1] = i
        d = {}
        for i in range(len(nums)-1 , -1 , -1):
            if nums[i] not in d:
                right[i] =0
                d[nums[i]] = [1 , i]
            else:
                r= d[nums[i]][0] * abs(i - d[nums[i]][1])  + right[d[nums[i]][1]]
                right[i] += r
                d[nums[i]][0] += 1
                d[nums[i]][1] = i
        tot = []
        for i in range(len(nums)):
            y=  left[i] + right[i]
            tot.append(y )
        return tot  





            




        
        