memo = {}
class Solution:

    def tribonacci(self, n: int) -> int:
        if n <2:
            return n
        if n ==2:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = self.tribonacci(n-3) + self.tribonacci(n -2) + self.tribonacci(n-1)
        return memo[n]
        
        