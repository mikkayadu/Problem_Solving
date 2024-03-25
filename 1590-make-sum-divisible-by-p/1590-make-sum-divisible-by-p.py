

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        cursum = 0; mini = len(nums)
        mydict = defaultdict(int)
        mydict[0] = -1
        
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        if p > total :
            return -1

        for i in range(len(nums)):
            cursum =( cursum + nums[i]) %p
            rem = (cursum - target) %p
            

            if rem in mydict:

                mini = min(mini, i - mydict[rem])
            mydict[cursum] = i

        return mini if mini < len(nums) else -1






        