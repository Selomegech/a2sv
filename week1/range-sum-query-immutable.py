class NumArray:

    def __init__(self, nums: List[int]):
        self.res = [0, nums[0]]
        self.summ = nums[0]

        for i in range(1, len(nums)):
            self.summ += nums[i]
            self.res.append(self.summ)

        

    def sumRange(self, left: int, right: int) -> int:
        return(self.res[right + 1]- self.res[left])
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)