class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if int(n) != n :
            return False
        if n == 1:
            return True
        if n<1:
            return False
        return self.isPowerOfThree(n/3)

        
