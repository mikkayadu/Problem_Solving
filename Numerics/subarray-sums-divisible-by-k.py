class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mydict = defaultdict(int); mydict[0] =1
        cursum = ans = 0

        for i in range(len(nums)):
            cursum += nums[i]
            rem = cursum % k

            
            ans += mydict[rem]

            mydict[rem] += 1
            
        return ans


            
        