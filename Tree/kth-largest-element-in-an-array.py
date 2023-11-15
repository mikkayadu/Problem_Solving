class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for value in nums:
            heappush(heap, value)

            if len(heap) > k:
                heappop(heap)
        return heap[0]
        