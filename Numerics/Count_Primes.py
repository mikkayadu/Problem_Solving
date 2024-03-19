class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        numbers = [1] * n
        numbers[0], numbers[1] = 0, 0

        for i in range(2, int(sqrt(n))+1):
            j =1
            if not numbers[i]:
                continue
            
            j = i ** 2

            while j < n:
                numbers[j] = 0
                j+=i
        return sum(numbers)
