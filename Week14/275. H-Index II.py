class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        low, high=0, len(citations) - 1

        while low <= high:
            mid = low + (high - low)//2
            
            if citations[mid] >= N-mid:
                high = mid - 1
            else:
                low = mid + 1
        # if citations[low] == 0:
        #     return 0
        return N-low
