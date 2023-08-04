class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        arr = []

        for i in range(n):
            ans = len(set(A[:i+1]).intersection(set(B[:i+1])))
            arr.append(ans)
        return arr
