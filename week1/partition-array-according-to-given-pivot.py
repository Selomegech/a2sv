class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result=[]
        less= [num for num in nums if num<pivot]
        more= [num for num in nums if num>pivot]
        for n in nums:
            if n==pivot:
                less.append(n)
        result= less+more 
        n = len(nums)//2
        
        return result

        