class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix =  [0] * (len(self.nums)+1)
        for i in range(len(self.nums)):
            self.prefix[i+1] = self.prefix[i] + self.nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        
        return self.prefix[right+1] - self.prefix[left]
