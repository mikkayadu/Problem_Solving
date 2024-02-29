class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        mydict = defaultdict(int)

        for num in arr:
            mydict[num] = mydict[num - difference] + 1
        return max(mydict.values())