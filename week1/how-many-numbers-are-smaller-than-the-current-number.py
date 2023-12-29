class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # result=[]
        # count=0
        # for i in range (len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] > nums[j]:
        #             count+=1
        #     result.append(count)
        #     count=0
        # return result
        count = [0] * 101
        for num in nums:
            count[num] += 1
        for i in range (1, len(count)):
            count[i]+=count[i-1]

        result=[]
        for num in nums:
            if num==0:
                result.append(0)
            else:
                result.append(count[num-1])
        return result