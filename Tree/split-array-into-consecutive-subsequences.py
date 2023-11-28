class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = []

        for num in nums:
            while heap and heap[0][0] < num -1 :
                if heappop(heap)[1]<3:
                    return False

            if heap and heap[0][0] == num -1 :
                val = heappop(heap)
                heappush(heap, [num, val[1] + 1])
            else:
                heappush(heap, [num, 1])

        for _, length  in heap:
            if length < 3:
                return False
        return True
                