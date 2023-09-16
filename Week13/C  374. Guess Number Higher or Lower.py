class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low<=high:
            mid = low + (high - low)//2

            val = guess(mid)
            if val == 0:
                return mid
            elif val == 1:
                low = mid + 1
            else:
                high = mid -1
        
