class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        return len(set([int("".join(reversed(str(num)))) for num in nums] + nums ))
        