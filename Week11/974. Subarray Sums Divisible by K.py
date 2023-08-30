class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        curSum = 0
        n = len(nums)
        mydict = {0:1}
        ans = 0

        for r in range(n):
            curSum += nums[r]
            modulo = curSum%k
            ans += mydict.get(modulo, 0)
            mydict[modulo] = mydict.get(modulo, 0) +1
        return ans
        
