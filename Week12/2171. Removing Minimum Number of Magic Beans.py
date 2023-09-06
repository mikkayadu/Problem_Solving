class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        total = sum(beans)
        beans.sort()
        minimum = float('inf')
        n = len(beans)
        for i in range(n):
            val = total - (beans[i] * (n-i))
            minimum = min(minimum, val)
        return minimum
