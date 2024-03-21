class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)
       
        def GCD(a, b):
            if b == 0:
                return a
            return GCD(b, a%b)
        return GCD(mini, maxi)